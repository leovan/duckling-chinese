# -*- coding: utf-8 -*-

import json
import unittest

from duckling_chinese import Duckling
from duckling_chinese.dimension import DucklingDimension
from ..utils import *


class RatingTestCase(unittest.TestCase):
    def setUp(self):
        self._duckling = Duckling()
        self._default_context = self._duckling.gen_context()

    def test_rating(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.RATING
            }
        )

        text = '评分8点5分'
        text_list = [
            '8.5分',
            '评分8.5'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('评分8点5分', entities[0]['body'])
        self.assertEqual('Rating', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(6, entities[0]['end'])
        self.assertEqual(8.5, entities[0]['value']['n'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '评分在8.5分以上'
        text_list = [
            '8.5分以上',
            '评分大于八点五'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('评分在8.5分以上', entities[0]['body'])
        self.assertEqual('Rating', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(9, entities[0]['end'])
        self.assertEqual(8.5, entities[0]['value']['start'])
        self.assertEqual('After', entities[0]['value']['direction'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '评分九点零以下'
        text_list = [
            '9分以下',
            '评分小于九'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('评分九点零以下', entities[0]['body'])
        self.assertEqual('Rating', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(7, entities[0]['end'])
        self.assertEqual(9.0, entities[0]['value']['start'])
        self.assertEqual('Before', entities[0]['value']['direction'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '评分在7到8.5分'
        text_list = [
            '评分在7到8.5',
            '评分在7到8.5分之间'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('评分在7到8.5分', entities[0]['body'])
        self.assertEqual('Rating', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(9, entities[0]['end'])
        self.assertEqual(7.0, entities[0]['value']['left'])
        self.assertEqual(8.5, entities[0]['value']['right'])
        self.assertEqual('Closed', entities[0]['value']['leftType'])
        self.assertEqual('Closed', entities[0]['value']['rightType'])

        self.assertTrue(has_same_value(entities, entities_list))


if __name__ == '__main__':
    unittest.main()
