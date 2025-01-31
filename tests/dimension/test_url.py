# -*- coding: utf-8 -*-

import json
import unittest

from duckling_chinese import Duckling
from duckling_chinese.dimension import DucklingDimension
from ..utils import *


class UrlTestCase(unittest.TestCase):
    def setUp(self):
        self._duckling = Duckling()
        self._default_context = self._duckling.gen_context()

    def test_url(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.URL
            }
        )

        text = 'http://www.bla.com'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('http://www.bla.com', entities[0]['body'])
        self.assertEqual('URL', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(18, entities[0]['end'])
        self.assertEqual('http://www.bla.com', entities[0]['value']['url'])
        self.assertEqual('bla.com', entities[0]['value']['domain'])
        self.assertEqual('http', entities[0]['value']['protocol'])

        text = 'www.bla.com:8080/path'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('www.bla.com:8080/path', entities[0]['body'])
        self.assertEqual('URL', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(21, entities[0]['end'])
        self.assertEqual('www.bla.com:8080/path', entities[0]['value']['url'])
        self.assertEqual('bla.com', entities[0]['value']['domain'])

        text = 'https://myserver?foo=bar'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('https://myserver?foo=bar', entities[0]['body'])
        self.assertEqual('URL', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(24, entities[0]['end'])
        self.assertEqual('https://myserver?foo=bar', entities[0]['value']['url'])
        self.assertEqual('myserver', entities[0]['value']['domain'])
        self.assertEqual('https', entities[0]['value']['protocol'])


if __name__ == '__main__':
    unittest.main()
