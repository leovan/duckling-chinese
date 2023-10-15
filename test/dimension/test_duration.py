# -*- coding: utf-8 -*-

import json
import unittest

from duckling_chinese import Duckling
from duckling_chinese.dimension import DucklingDimension
from ..utils import *


class ActTestCase(unittest.TestCase):
    def setUp(self):
        self._duckling = Duckling()
        self._default_context = self._duckling.gen_context()

    def test_act(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.DURATION
            }
        )

        text = '1秒钟'
        text_list = ['1秒']
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('1秒钟', entities[0]['body'])
        self.assertEqual('Duration', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(3, entities[0]['end'])
        self.assertEqual(1, entities[0]['value']['value'])
        self.assertEqual('Second', entities[0]['value']['grain'])
        self.assertFalse(entities[0]['value']['latent'])
        self.assertFalse(entities[0]['value']['fuzzy'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '1分09秒'
        text_list = ['一分零九秒', '一分九秒']
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('1分09秒', entities[0]['body'])
        self.assertEqual('Duration', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(5, entities[0]['end'])
        self.assertEqual(69, entities[0]['value']['value'])
        self.assertEqual('Second', entities[0]['value']['grain'])
        self.assertFalse(entities[0]['value']['latent'])
        self.assertFalse(entities[0]['value']['fuzzy'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '1小时09分'
        text_list = ['1小时9分', '一小时零九分', '一小时九分']
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('1小时09分', entities[0]['body'])
        self.assertEqual('Duration', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(6, entities[0]['end'])
        self.assertEqual(69, entities[0]['value']['value'])
        self.assertEqual('Minute', entities[0]['value']['grain'])
        self.assertFalse(entities[0]['value']['latent'])
        self.assertFalse(entities[0]['value']['fuzzy'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '30天'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('30天', entities[0]['body'])
        self.assertEqual('Duration', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(3, entities[0]['end'])
        self.assertEqual(30, entities[0]['value']['value'])
        self.assertEqual('Day', entities[0]['value']['grain'])
        self.assertFalse(entities[0]['value']['latent'])
        self.assertFalse(entities[0]['value']['fuzzy'])

        text = '七周'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('七周', entities[0]['body'])
        self.assertEqual('Duration', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(2, entities[0]['end'])
        self.assertEqual(7, entities[0]['value']['value'])
        self.assertEqual('Week', entities[0]['value']['grain'])
        self.assertFalse(entities[0]['value']['latent'])
        self.assertFalse(entities[0]['value']['fuzzy'])

        text = '一个月'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('一个月', entities[0]['body'])
        self.assertEqual('Duration', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(3, entities[0]['end'])
        self.assertEqual(1, entities[0]['value']['value'])
        self.assertEqual('Month', entities[0]['value']['grain'])
        self.assertFalse(entities[0]['value']['latent'])
        self.assertFalse(entities[0]['value']['fuzzy'])

        text = '3个季度'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('3个季度', entities[0]['body'])
        self.assertEqual('Duration', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(4, entities[0]['end'])
        self.assertEqual(3, entities[0]['value']['value'])
        self.assertEqual('Quarter', entities[0]['value']['grain'])
        self.assertFalse(entities[0]['value']['latent'])
        self.assertFalse(entities[0]['value']['fuzzy'])

        text = '两年'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('两年', entities[0]['body'])
        self.assertEqual('Duration', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(2, entities[0]['end'])
        self.assertEqual(2, entities[0]['value']['value'])
        self.assertEqual('Year', entities[0]['value']['grain'])
        self.assertFalse(entities[0]['value']['latent'])
        self.assertFalse(entities[0]['value']['fuzzy'])

        text = '两年零三个月'
        text_list = [
            '两年外加三个月',
            '两年加上三个月',
            '两年加三个月',
            '两年三个月'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('两年零三个月', entities[0]['body'])
        self.assertEqual('Duration', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(6, entities[0]['end'])
        self.assertEqual(27, entities[0]['value']['value'])
        self.assertEqual('Month', entities[0]['value']['grain'])
        self.assertFalse(entities[0]['value']['latent'])
        self.assertFalse(entities[0]['value']['fuzzy'])

        self.assertTrue(has_same_value(entities, entities_list))


if __name__ == '__main__':
    unittest.main()
