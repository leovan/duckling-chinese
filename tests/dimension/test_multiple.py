# -*- coding: utf-8 -*-

import json
import unittest

from duckling_chinese import Duckling
from duckling_chinese.dimension import DucklingDimension
from ..utils import *


class MultipleTestCase(unittest.TestCase):
    def setUp(self):
        self._duckling = Duckling()
        self._default_context = self._duckling.gen_context()

    def test_multiple(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.MULTIPLE
            }
        )

        text = '8点5倍'
        text_list = ['8.5倍']
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('8点5倍', entities[0]['body'])
        self.assertEqual('Multiple', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(4, entities[0]['end'])
        self.assertEqual(8.5, entities[0]['value']['n'])

        self.assertTrue(has_same_value(entities, entities_list))


if __name__ == '__main__':
    unittest.main()
