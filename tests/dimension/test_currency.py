# -*- coding: utf-8 -*-

import json
import unittest

from duckling_chinese import Duckling
from duckling_chinese.dimension import DucklingDimension
from ..utils import *


class CurrencyTestCase(unittest.TestCase):
    def setUp(self):
        self._duckling = Duckling()
        self._default_context = self._duckling.gen_context()

    def test_area(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.CURRENCY
            }
        )

        text = '九十九元九角九分'
        text_list = ['九十九块九毛九']
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('九十九元九角九分', entities[0]['body'])
        self.assertEqual('Currency', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(8, entities[0]['end'])
        self.assertEqual(99.99, entities[0]['value']['v'])
        self.assertEqual('货币:CNY', entities[0]['value']['dim'])
        self.assertEqual('元', entities[0]['value']['unit'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '九十九块九'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('九十九块九', entities[0]['body'])
        self.assertEqual('Currency', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(5, entities[0]['end'])
        self.assertEqual(99.9, entities[0]['value']['v'])
        self.assertEqual('货币:CNY', entities[0]['value']['dim'])
        self.assertEqual('元', entities[0]['value']['unit'])

        text = '九块九'
        text_list = ['九元九角']
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('九块九', entities[0]['body'])
        self.assertEqual('Currency', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(3, entities[0]['end'])
        self.assertEqual(9.9, entities[0]['value']['v'])
        self.assertEqual('货币:CNY', entities[0]['value']['dim'])
        self.assertEqual('元', entities[0]['value']['unit'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '九元零九分'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('九元零九分', entities[0]['body'])
        self.assertEqual('Currency', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(5, entities[0]['end'])
        self.assertEqual(9.09, entities[0]['value']['v'])
        self.assertEqual('货币:CNY', entities[0]['value']['dim'])
        self.assertEqual('元', entities[0]['value']['unit'])

        text = '九角九分'
        text_list = ['九毛九']
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('九角九分', entities[0]['body'])
        self.assertEqual('Currency', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(4, entities[0]['end'])
        self.assertEqual(0.99, entities[0]['value']['v'])
        self.assertEqual('货币:CNY', entities[0]['value']['dim'])
        self.assertEqual('元', entities[0]['value']['unit'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '九毛钱'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('九毛钱', entities[0]['body'])
        self.assertEqual('Currency', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(3, entities[0]['end'])
        self.assertEqual(0.9, entities[0]['value']['v'])
        self.assertEqual('货币:CNY', entities[0]['value']['dim'])
        self.assertEqual('元', entities[0]['value']['unit'])

        text = '九分钱'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('九分钱', entities[0]['body'])
        self.assertEqual('Currency', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(3, entities[0]['end'])
        self.assertEqual(0.09, entities[0]['value']['v'])
        self.assertEqual('货币:CNY', entities[0]['value']['dim'])
        self.assertEqual('元', entities[0]['value']['unit'])

        text = '两块九毛九'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('两块九毛九', entities[0]['body'])
        self.assertEqual('Currency', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(5, entities[0]['end'])
        self.assertEqual(2.99, entities[0]['value']['v'])
        self.assertEqual('货币:CNY', entities[0]['value']['dim'])
        self.assertEqual('元', entities[0]['value']['unit'])

        text = 'RMB两块九毛九'
        text_list = ['两块九毛九RMB']
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('RMB两块九毛九', entities[0]['body'])
        self.assertEqual('Currency', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(8, entities[0]['end'])
        self.assertEqual(2.99, entities[0]['value']['v'])
        self.assertEqual('货币:CNY', entities[0]['value']['dim'])
        self.assertEqual('元', entities[0]['value']['unit'])

        self.assertTrue(has_same_value(entities, entities_list))


if __name__ == '__main__':
    unittest.main()
