# -*- coding: utf-8 -*-

import json
import unittest

from duckling_chinese import Duckling
from duckling_chinese.dimension import DucklingDimension
from ..utils import *


class LyricTestCase(unittest.TestCase):
    def setUp(self):
        self._duckling = Duckling()
        self._default_context = self._duckling.gen_context()

    def test_lyric(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.LYRIC
            }
        )

        text = '作曲:刘德华'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('作曲:刘德华', entities[0]['body'])
        self.assertEqual('Lyric', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(6, entities[0]['end'])
        self.assertEqual(['刘德华'], entities[0]['value']['roles']['作曲'])

        text = '作曲-编曲:刘德华'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('作曲-编曲:刘德华', entities[0]['body'])
        self.assertEqual('Lyric', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(9, entities[0]['end'])
        self.assertEqual(['刘德华'], entities[0]['value']['roles']['编曲'])
        self.assertEqual(['刘德华'], entities[0]['value']['roles']['作曲'])

        text = '作曲:张三 作词:李四'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('作曲:张三 作词:李四', entities[0]['body'])
        self.assertEqual('Lyric', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(11, entities[0]['end'])
        self.assertEqual(['张三'], entities[0]['value']['roles']['作曲'])
        self.assertEqual(['李四'], entities[0]['value']['roles']['作词'])

        text = '编曲:墨辞  词: 刀郎'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('编曲:墨辞  词: 刀郎', entities[0]['body'])
        self.assertEqual('Lyric', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(12, entities[0]['end'])
        self.assertEqual(['墨辞'], entities[0]['value']['roles']['编曲'])
        self.assertEqual(['刀郎'], entities[0]['value']['roles']['作词'])

        text = '编曲:墨辞  词: 刀郎 曲 周杰伦'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('编曲:墨辞  词: 刀郎 曲 周杰伦', entities[0]['body'])
        self.assertEqual('Lyric', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(18, entities[0]['end'])
        self.assertEqual(['周杰伦'], entities[0]['value']['roles']['作曲'])
        self.assertEqual(['刀郎'], entities[0]['value']['roles']['作词'])
        self.assertEqual(['墨辞'], entities[0]['value']['roles']['编曲'])

        text = '作词:爱内里菜/作曲/编曲:corin'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('作词:爱内里菜/作曲/编曲:corin', entities[0]['body'])
        self.assertEqual('Lyric', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(19, entities[0]['end'])
        self.assertEqual(['corin'], entities[0]['value']['roles']['作曲'])
        self.assertEqual(['爱内里菜'], entities[0]['value']['roles']['作词'])
        self.assertEqual(['corin'], entities[0]['value']['roles']['编曲'])

        text = '作曲:黄耀光|填词:林夕'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('作曲:黄耀光|填词:林夕', entities[0]['body'])
        self.assertEqual('Lyric', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(12, entities[0]['end'])
        self.assertEqual(['黄耀光'], entities[0]['value']['roles']['作曲'])
        self.assertEqual(['林夕'], entities[0]['value']['roles']['作词'])


if __name__ == '__main__':
    unittest.main()
