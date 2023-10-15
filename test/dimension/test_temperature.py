# -*- coding: utf-8 -*-

import json
import unittest

from duckling_chinese import Duckling
from duckling_chinese.dimension import DucklingDimension
from ..utils import *


class TemperatureTestCase(unittest.TestCase):
    def setUp(self):
        self._duckling = Duckling()
        self._default_context = self._duckling.gen_context()

    def test_temperature(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.TEMPERATURE
            }
        )

        text = '摄氏30度'
        text_list = [
            '30摄氏度',
            '三十度',
            '三十°',
            '30°C'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('摄氏30度', entities[0]['body'])
        self.assertEqual('Temperature', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(5, entities[0]['end'])
        self.assertEqual(30.0, entities[0]['value']['v'])
        self.assertEqual('温度', entities[0]['value']['dim'])
        self.assertEqual('C', entities[0]['value']['unit'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '零下华氏三十一度半'
        text_list = [
            '华氏零下三十一度半',
            '华氏-31度半'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('零下华氏三十一度半', entities[0]['body'])
        self.assertEqual('Temperature', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(9, entities[0]['end'])
        self.assertEqual(-31.5, entities[0]['value']['v'])
        self.assertEqual('温度', entities[0]['value']['dim'])
        self.assertEqual('F', entities[0]['value']['unit'])

        self.assertTrue(has_same_value(entities, entities_list))


if __name__ == '__main__':
    unittest.main()
