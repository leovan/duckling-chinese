# -*- coding: utf-8 -*-

import json
import unittest

from duckling_chinese import Duckling
from duckling_chinese.dimension import DucklingDimension
from ..utils import *


class AreaTestCase(unittest.TestCase):
    def setUp(self):
        self._duckling = Duckling()
        self._default_context = self._duckling.gen_context()

    def test_area(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.AREA
            }
        )

        text = '三平方'
        text_list = ['三平方米', '三个平方', '三平米', '三平']
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('三平方', entities[0]['body'])
        self.assertEqual('Area', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(3, entities[0]['end'])
        self.assertEqual(3.0, entities[0]['value']['v'])
        self.assertEqual('Area', entities[0]['value']['dim'])
        self.assertEqual('平方米', entities[0]['value']['unit'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '三平方千米'
        text_list = ['三平方公里']
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('三平方千米', entities[0]['body'])
        self.assertEqual('Area', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(5, entities[0]['end'])
        self.assertEqual(3.0, entities[0]['value']['v'])
        self.assertEqual('Area', entities[0]['value']['dim'])
        self.assertEqual('平方千米', entities[0]['value']['unit'])

        self.assertTrue(has_same_value(entities, entities_list))


if __name__ == '__main__':
    unittest.main()
