# -*- coding: utf-8 -*-

import json
import unittest

from duckling_chinese import Duckling
from duckling_chinese.dimension import DucklingDimension
from ..utils import *


class DuplicateTestCase(unittest.TestCase):
    def setUp(self):
        self._duckling = Duckling()
        self._default_context = self._duckling.gen_context()

    def test_duplicate(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.DUPLICATE
            }
        )

        text = '张三张三张三'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('张三张三张三', entities[0]['body'])
        self.assertEqual('Duplicate', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(6, entities[0]['end'])
        self.assertEqual('张三', entities[0]['value']['w'])
        self.assertEqual(3, entities[0]['value']['times'])

        text = '123123123'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('123123123', entities[0]['body'])
        self.assertEqual('Duplicate', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(9, entities[0]['end'])
        self.assertEqual('123', entities[0]['value']['w'])
        self.assertEqual(3, entities[0]['value']['times'])


if __name__ == '__main__':
    unittest.main()
