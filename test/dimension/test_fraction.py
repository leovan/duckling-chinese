# -*- coding: utf-8 -*-

import json
import unittest

from duckling_chinese import Duckling
from duckling_chinese.dimension import DucklingDimension
from ..utils import *


class FractionTestCase(unittest.TestCase):
    def setUp(self):
        self._duckling = Duckling()
        self._default_context = self._duckling.gen_context()

    def test_fraction(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.FRACTION
            }
        )

        text = '百分之六十'
        text_list = ['60%']
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('百分之六十', entities[0]['body'])
        self.assertEqual('Fraction', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(5, entities[0]['end'])
        self.assertEqual(0.6, entities[0]['value']['n'])
        self.assertEqual(60.0, entities[0]['value']['numerator'])
        self.assertEqual(100.0, entities[0]['value']['denominator'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '4分之3'
        text_list = ['四分之3', '3/4']
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('4分之3', entities[0]['body'])
        self.assertEqual('Fraction', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(4, entities[0]['end'])
        self.assertEqual(0.75, entities[0]['value']['n'])
        self.assertEqual(3.0, entities[0]['value']['numerator'])
        self.assertEqual(4.0, entities[0]['value']['denominator'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '负百分之百'
        text_list = ['负的百分之百', '负的百分之一百']
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('负百分之百', entities[0]['body'])
        self.assertEqual('Fraction', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(5, entities[0]['end'])
        self.assertEqual(-1.0, entities[0]['value']['n'])
        self.assertEqual(100.0, entities[0]['value']['numerator'])
        self.assertEqual(-100.0, entities[0]['value']['denominator'])

        self.assertTrue(has_same_value(entities, entities_list))


if __name__ == '__main__':
    unittest.main()
