# -*- coding: utf-8 -*-

import json
import unittest

from duckling_chinese import Duckling
from duckling_chinese.dimension import DucklingDimension
from ..utils import *


class AgeTestCase(unittest.TestCase):
    def setUp(self):
        self._duckling = Duckling()
        self._default_context = self._duckling.gen_context()

    def test_act(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.AGE
            }
        )

        text = '三岁'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('三岁', entities[0]['body'])
        self.assertEqual('Age', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(2, entities[0]['end'])
        self.assertEqual(3.0, entities[0]['value']['n'])

        text = '三岁半以上'
        text_list = ['大于三岁半']
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('三岁半以上', entities[0]['body'])
        self.assertEqual('Age', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(5, entities[0]['end'])
        self.assertEqual(3.5, entities[0]['value']['start'])
        self.assertEqual('After', entities[0]['value']['direction'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '三岁半以下'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('三岁半以下', entities[0]['body'])
        self.assertEqual('Age', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(5, entities[0]['end'])
        self.assertEqual(3.5, entities[0]['value']['start'])
        self.assertEqual('Before', entities[0]['value']['direction'])

        text = '三到五岁半'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('三到五岁半', entities[0]['body'])
        self.assertEqual('Age', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(5, entities[0]['end'])
        self.assertEqual(3.0, entities[0]['value']['left'])
        self.assertEqual(5.5, entities[0]['value']['right'])
        self.assertEqual('Closed', entities[0]['value']['leftType'])
        self.assertEqual('Closed', entities[0]['value']['rightType'])

        text = '三到五岁'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('三到五岁', entities[0]['body'])
        self.assertEqual('Age', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(4, entities[0]['end'])
        self.assertEqual(3.0, entities[0]['value']['left'])
        self.assertEqual(5.0, entities[0]['value']['right'])
        self.assertEqual('Closed', entities[0]['value']['leftType'])
        self.assertEqual('Closed', entities[0]['value']['rightType'])


if __name__ == '__main__':
    unittest.main()
