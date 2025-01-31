# -*- coding: utf-8 -*-

import json
import unittest

from duckling_chinese import Duckling
from duckling_chinese.dimension import DucklingDimension
from ..utils import *


class NumeralTestCase(unittest.TestCase):
    def setUp(self):
        self._duckling = Duckling()
        self._default_context = self._duckling.gen_context()

    def test_numeral(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.NUMERAL
            }
        )

        text = '0'
        text_list = ['〇', '零']
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('0', entities[0]['body'])
        self.assertEqual('Numeral', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(1, entities[0]['end'])
        self.assertEqual(0.0, entities[0]['value']['n'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = 'Ⅲ'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('Ⅲ', entities[0]['body'])
        self.assertEqual('Numeral', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(1, entities[0]['end'])
        self.assertEqual(3.0, entities[0]['value']['n'])

        text = '-1200000'
        text_list = [
            '- 1,200,000',
            '负1,200,000',
            '负 1,200,000',
            '负1200000',
            '负 1200000',
            '-1.2M',
            '-1200K',
            '-.0012G',
            '负一百二十万'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('-1200000', entities[0]['body'])
        self.assertEqual('Numeral', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(8, entities[0]['end'])
        self.assertEqual(-1200000.0, entities[0]['value']['n'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '1点45'
        text_list = [
            '一点四五'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('1点45', entities[0]['body'])
        self.assertEqual('Numeral', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(4, entities[0]['end'])
        self.assertEqual(1.45, entities[0]['value']['n'])

        self.assertTrue(has_same_value(entities, entities_list))


if __name__ == '__main__':
    unittest.main()
