# -*- coding: utf-8 -*-

import json
import unittest

from duckling_chinese import Duckling
from duckling_chinese.dimension import DucklingDimension
from ..utils import *


class VelocityTestCase(unittest.TestCase):
    def setUp(self):
        self._duckling = Duckling()
        self._default_context = self._duckling.gen_context()

    def test_velocity(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.VELOCITY
            }
        )

        text = '3千米每小时'
        text_list = [
            '每小时3千米',
            '3公里每小时',
            '每小时3公里'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('3千米每小时', entities[0]['body'])
        self.assertEqual('Velocity', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(6, entities[0]['end'])
        self.assertEqual(3.0, entities[0]['value']['v'])
        self.assertEqual('Velocity', entities[0]['value']['dim'])
        self.assertEqual('千米每小时', entities[0]['value']['unit'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '0.8米每秒'
        text_list = [
            '每秒0.8米'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('0.8米每秒', entities[0]['body'])
        self.assertEqual('Velocity', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(6, entities[0]['end'])
        self.assertEqual(0.8, entities[0]['value']['v'])
        self.assertEqual('Velocity', entities[0]['value']['dim'])
        self.assertEqual('米每秒', entities[0]['value']['unit'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '1.8英里每小时'
        text_list = [
            '1.8迈',
            '1.8码'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('1.8英里每小时', entities[0]['body'])
        self.assertEqual('Velocity', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(8, entities[0]['end'])
        self.assertEqual(1.8, entities[0]['value']['v'])
        self.assertEqual('Velocity', entities[0]['value']['dim'])
        self.assertEqual('英里每小时', entities[0]['value']['unit'])

        self.assertTrue(has_same_value(entities, entities_list))


if __name__ == '__main__':
    unittest.main()
