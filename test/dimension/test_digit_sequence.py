# -*- coding: utf-8 -*-

import json
import unittest

from duckling_chinese import Duckling
from duckling_chinese.dimension import DucklingDimension
from ..utils import *


class DigitSequenceTestCase(unittest.TestCase):
    def setUp(self):
        self._duckling = Duckling()
        self._default_context = self._duckling.gen_context()

    def test_act(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.DIGIT_SEQUENCE
            }
        )

        text = '011'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('011', entities[0]['body'])
        self.assertEqual('DigitSequence', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(3, entities[0]['end'])
        self.assertEqual('011', entities[0]['value']['seq'])
        self.assertFalse(entities[0]['value']['zh'])

        text = '零一幺'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('零一幺', entities[0]['body'])
        self.assertEqual('DigitSequence', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(3, entities[0]['end'])
        self.assertEqual('011', entities[0]['value']['seq'])
        self.assertTrue(entities[0]['value']['zh'])
        self.assertEqual('零一幺', entities[0]['value']['raw'])


if __name__ == '__main__':
    unittest.main()
