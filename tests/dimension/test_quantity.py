# -*- coding: utf-8 -*-

import json
import unittest

from duckling_chinese import Duckling
from duckling_chinese.dimension import DucklingDimension
from ..utils import *


class QuantityTestCase(unittest.TestCase):
    def setUp(self):
        self._duckling = Duckling()
        self._default_context = self._duckling.gen_context()

    def test_quantity(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.QUANTITY
            }
        )

        text = '一千米'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('一千米', entities[0]['body'])
        self.assertEqual('Quantity', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(3, entities[0]['end'])
        self.assertEqual(1.0, entities[0]['value']['v'])
        self.assertEqual('?', entities[0]['value']['dim'])
        self.assertEqual('千米', entities[0]['value']['unit'])

        text = '三千千瓦时'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('三千千瓦时', entities[0]['body'])
        self.assertEqual('Quantity', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(5, entities[0]['end'])
        self.assertEqual(3000.0, entities[0]['value']['v'])
        self.assertEqual('?', entities[0]['value']['dim'])
        self.assertEqual('千瓦时', entities[0]['value']['unit'])


if __name__ == '__main__':
    unittest.main()
