# -*- coding: utf-8 -*-

import json
import unittest

from duckling_chinese import Duckling
from duckling_chinese.dimension import DucklingDimension
from ..utils import *


class MultiCharTestCase(unittest.TestCase):
    def setUp(self):
        self._duckling = Duckling()
        self._default_context = self._duckling.gen_context()

    def test_multi_char(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.MULTI_CHAR
            }
        )

        text = '👄'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('👄', entities[0]['body'])
        self.assertEqual('MultiChar', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(2, entities[0]['end'])
        self.assertEqual('👄', entities[0]['value']['text'])
        self.assertTrue(entities[0]['value']['isEmoji'])
        self.assertEqual(':lips:', entities[0]['value']['aliasOfEmoji'])


if __name__ == '__main__':
    unittest.main()
