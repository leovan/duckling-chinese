# -*- coding: utf-8 -*-

import json
import unittest

from duckling_chinese import Duckling
from duckling_chinese.dimension import DucklingDimension
from ..utils import *


class PhoneNumberTestCase(unittest.TestCase):
    def setUp(self):
        self._duckling = Duckling()
        self._default_context = self._duckling.gen_context()

    def test_phone_number(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.PHONE_NUMBER
            }
        )

        text = '(+1)650-701-8887'
        text_list = [
            '(+1)   650 - 701  8887',
            '(+1) 650-701-8887',
            '+1 650.701.8887'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('(+1)650-701-8887', entities[0]['body'])
        self.assertEqual('PhoneNumber', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(16, entities[0]['end'])
        self.assertEqual('6507018887', entities[0]['value']['number'])
        self.assertEqual('1', entities[0]['value']['area'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '(650)-701-8887 ext 897'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('(650)-701-8887 ext 897', entities[0]['body'])
        self.assertEqual('PhoneNumber', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(22, entities[0]['end'])
        self.assertEqual('6507018887', entities[0]['value']['number'])
        self.assertEqual('897', entities[0]['value']['ext'])


if __name__ == '__main__':
    unittest.main()
