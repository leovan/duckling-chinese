# -*- coding: utf-8 -*-

import json
import unittest

from duckling_chinese import Duckling
from duckling_chinese.dimension import DucklingDimension


class ConstellationTestCase(unittest.TestCase):
    def setUp(self):
        self._duckling = Duckling()
        self._default_context = self._duckling.gen_context()

    def test_constellation(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.CONSTELLATION
            }
        )
        latent_options = self._duckling.gen_options(
            with_latent=True,
            targets={
                DucklingDimension.CONSTELLATION
            }
        )

        text = '双子座'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('双子座', entities[0]['body'])
        self.assertEqual('Constellation', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(3, entities[0]['end'])
        self.assertEqual('双子座', entities[0]['value']['w'])
        self.assertFalse(entities[0]['value']['latent'])

        text = '魔蝎'
        entities = self._duckling.parse_entities(
            text, self._default_context, latent_options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('魔蝎', entities[0]['body'])
        self.assertEqual('Constellation', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(2, entities[0]['end'])
        self.assertEqual('摩羯座', entities[0]['value']['w'])
        self.assertTrue(entities[0]['value']['latent'])


if __name__ == '__main__':
    unittest.main()
