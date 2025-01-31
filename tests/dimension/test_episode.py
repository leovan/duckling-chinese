# -*- coding: utf-8 -*-

import json
import unittest

from duckling_chinese import Duckling
from duckling_chinese.dimension import DucklingDimension
from ..utils import *


class EpisodeTestCase(unittest.TestCase):
    def setUp(self):
        self._duckling = Duckling()
        self._default_context = self._duckling.gen_context()

    def test_episode(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.EPISODE
            }
        )

        text = '倒数第一集'
        text_list = ['最后一集']
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('倒数第一集', entities[0]['body'])
        self.assertEqual('Episode', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(5, entities[0]['end'])
        self.assertEqual(-1.0, entities[0]['value']['v'])
        self.assertEqual('集', entities[0]['value']['dim'])
        self.assertEqual('集', entities[0]['value']['unit'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '第三集'
        text_list = ['第三期', '第三回']
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('第三集', entities[0]['body'])
        self.assertEqual('Episode', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(3, entities[0]['end'])
        self.assertEqual(3.0, entities[0]['value']['v'])
        self.assertEqual('集', entities[0]['value']['dim'])
        self.assertEqual('集', entities[0]['value']['unit'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '第一百一十一期'
        text_list = ['111集']
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('第一百一十一期', entities[0]['body'])
        self.assertEqual('Episode', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(7, entities[0]['end'])
        self.assertEqual(111.0, entities[0]['value']['v'])
        self.assertEqual('集', entities[0]['value']['dim'])
        self.assertEqual('集', entities[0]['value']['unit'])

        self.assertTrue(has_same_value(entities, entities_list))


if __name__ == '__main__':
    unittest.main()
