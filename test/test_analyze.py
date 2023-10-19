# -*- coding: utf-8 -*-

import unittest

from duckling_chinese import Duckling
from duckling_chinese.dimension import DucklingDimension


class AnalyzeTestCase(unittest.TestCase):
    def setUp(self):
        self._duckling = Duckling()
        self._default_context = self._duckling.gen_context()

    def test_analyze(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.LYRIC
            }
        )

        text = '编曲:墨辞  词: 刀郎 曲 周杰伦'
        answers = self._duckling.analyze(
            text, self._default_context, options)
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        self.assertEqual(2, len(answers))
        self.assertEqual(1, len(entities))


if __name__ == '__main__':
    unittest.main()
