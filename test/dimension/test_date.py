# -*- coding: utf-8 -*-

import json
import unittest

from datetime import datetime

try:
    from zoneinfo import ZoneInfo
except ImportError:
    from backports.zoneinfo import ZoneInfo

from duckling_chinese import Duckling
from duckling_chinese.dimension import DucklingDimension
from ..utils import *


class DateTestCase(unittest.TestCase):
    def setUp(self):
        self._duckling = Duckling()
        self._default_context = self._duckling.gen_context(
            reference_time=datetime(
                year=2013,
                month=2,
                day=12,
                hour=4,
                minute=30,
                second=0,
                tzinfo=ZoneInfo('Asia/Shanghai')))

    def test_date(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.DATE
            }
        )

        text = '2015-3-3'
        text_list = [
            '2015-03-03',
            '20150303',
            '2015/3/3',
            '2015.3.3',
            '15.3.3',
            '2015年3月3号',
            '2015年3月三号',
            '2015年三月3号',
            '2015年三月三号'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('2015-3-3', entities[0]['body'])
        self.assertEqual('Date', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(8, entities[0]['end'])
        self.assertEqual('2015-03-03 00:00:00 [UTC+08:00]', entities[0]['value']['timeValue']['instant']['datetime'])
        self.assertEqual('Day', entities[0]['value']['timeValue']['instant']['grain'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '2015年'
        text_list = [
            '2015版',
            '2015年版',
            '15年',
            '15版',
            '15年版',
            '一五年',
            '一五版',
            '一五年版',
            '二零一五年'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('2015年', entities[0]['body'])
        self.assertEqual('Date', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(5, entities[0]['end'])
        self.assertEqual('2015-01-01 00:00:00 [UTC+08:00]', entities[0]['value']['timeValue']['instant']['datetime'])
        self.assertEqual('Year', entities[0]['value']['timeValue']['instant']['grain'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '03/03'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('03/03', entities[0]['body'])
        self.assertEqual('Date', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(5, entities[0]['end'])
        self.assertEqual('2013-03-03 00:00:00 [UTC+08:00]', entities[0]['value']['timeValue']['instant']['datetime'])
        self.assertEqual('Day', entities[0]['value']['timeValue']['instant']['grain'])

        text = '月底'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('月底', entities[0]['body'])
        self.assertEqual('Date', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(2, entities[0]['end'])
        self.assertEqual('2013-02-28 00:00:00 [UTC+08:00]', entities[0]['value']['timeValue']['instant']['datetime'])
        self.assertEqual('Day', entities[0]['value']['timeValue']['instant']['grain'])

        text = '农历一月十八'
        text_list = [
            '正月十八',
            '农历的一月十八',
            '阴历的正月十八'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('农历一月十八', entities[0]['body'])
        self.assertEqual('Date', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(6, entities[0]['end'])
        self.assertEqual('农历 二〇一三年正月十八 00:00:00 [UTC+08:00]', entities[0]['value']['timeValue']['instant']['datetime'])
        self.assertEqual('Day', entities[0]['value']['timeValue']['instant']['grain'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '今明后三天'
        text_list = [
            '今天明天后天三天'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('今明后三天', entities[0]['body'])
        self.assertEqual('Date', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(5, entities[0]['end'])
        self.assertEqual('2013-02-12 00:00:00 [UTC+08:00]', entities[0]['value']['timeValue']['start']['datetime'])
        self.assertEqual('Day', entities[0]['value']['timeValue']['start']['grain'])
        self.assertEqual('2013-02-15 00:00:00 [UTC+08:00]', entities[0]['value']['timeValue']['end']['datetime'])
        self.assertEqual('Day', entities[0]['value']['timeValue']['end']['grain'])


if __name__ == '__main__':
    unittest.main()
