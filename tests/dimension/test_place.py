# -*- coding: utf-8 -*-

import json
import unittest

from duckling_chinese import Duckling
from duckling_chinese.dimension import DucklingDimension
from ..utils import *


class PlaceTestCase(unittest.TestCase):
    def setUp(self):
        self._duckling = Duckling()
        self._default_context = self._duckling.gen_context()

    def test_place(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.PLACE
            }
        )

        text = '湖北当阳'
        text_list = [
            '当阳市',
            '湖北省当阳市',
            '当阳县'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('湖北当阳', entities[0]['body'])
        self.assertEqual('Place', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(4, entities[0]['end'])
        self.assertEqual(5841, entities[0]['value']['candidates'][0]['id'])
        self.assertEqual('区县', entities[0]['value']['candidates'][0]['category'])
        self.assertEqual('当阳市', entities[0]['value']['candidates'][0]['name'])
        self.assertEqual(['当阳'], entities[0]['value']['candidates'][0]['alias'])
        self.assertEqual('当阳市', entities[0]['value']['candidates'][0]['name'])
        self.assertEqual('420582000000', entities[0]['value']['candidates'][0]['code'])
        self.assertEqual(3832, entities[0]['value']['candidates'][0]['partOf'])
        self.assertFalse(entities[0]['value']['isBirthPlace'])

        self.assertTrue(has_same_value(entities, entities_list))


if __name__ == '__main__':
    unittest.main()
