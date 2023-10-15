# -*- coding: utf-8 -*-

import json
import unittest

from duckling_chinese import Duckling
from duckling_chinese.dimension import DucklingDimension
from ..utils import *


class DistanceTestCase(unittest.TestCase):
    def setUp(self):
        self._duckling = Duckling()
        self._default_context = self._duckling.gen_context()

    def test_diatance(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.DISTANCE
            }
        )

        text = '3千米'
        text_list = ['三公里', '3km', '3000米', '3000m']
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('3千米', entities[0]['body'])
        self.assertEqual('Distance', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(3, entities[0]['end'])
        self.assertEqual(3000.0, entities[0]['value']['v'])
        self.assertEqual('Distance', entities[0]['value']['dim'])
        self.assertEqual('米', entities[0]['value']['unit'])

        self.assertTrue(has_same_value(entities, entities_list))


if __name__ == '__main__':
    unittest.main()
