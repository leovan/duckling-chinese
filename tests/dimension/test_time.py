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


class TimeTestCase(unittest.TestCase):
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

    def test_time(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.TIME
            }
        )

        text = '现在'
        text_list = [
            '此时',
            '此刻',
            '当前',
            '04:30:00'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('现在', entities[0]['body'])
        self.assertEqual('Time', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(2, entities[0]['end'])
        self.assertEqual('2013-02-12 04:30:00 [UTC+08:00]', entities[0]['value']['timeValue']['instant']['datetime'])
        self.assertEqual('Second', entities[0]['value']['timeValue']['instant']['grain'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '下午三点十五'
        text_list = [
            '下午3:15',
            '15:15',
            '3:15pm',
            '3:15p.m',
            '下午三点一刻',
            '下午的三点一刻'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('下午三点十五', entities[0]['body'])
        self.assertEqual('Time', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(6, entities[0]['end'])
        self.assertEqual('2013-02-12 15:15:00 [UTC+08:00]', entities[0]['value']['timeValue']['instant']['datetime'])
        self.assertEqual('Minute', entities[0]['value']['timeValue']['instant']['grain'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '明天晚上12点'
        text_list = [
            '13号晚上12点',
            '13号晚12点'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('明天晚上12点', entities[0]['body'])
        self.assertEqual('Time', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(7, entities[0]['end'])
        self.assertEqual('2013-02-14 00:00:00 [UTC+08:00]', entities[0]['value']['timeValue']['instant']['datetime'])
        self.assertEqual('Hour', entities[0]['value']['timeValue']['instant']['grain'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '今早6点'
        text_list = [
            '今天早上6点',
            '12号早上6点',
            '12号早6点'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('今早6点', entities[0]['body'])
        self.assertEqual('Time', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(4, entities[0]['end'])
        self.assertEqual('2013-02-12 06:00:00 [UTC+08:00]', entities[0]['value']['timeValue']['instant']['datetime'])
        self.assertEqual('Hour', entities[0]['value']['timeValue']['instant']['grain'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '明天10点'
        text_list = [
            '明天上午十点',
            '明天中午10点'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('明天10点', entities[0]['body'])
        self.assertEqual('Time', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(5, entities[0]['end'])
        self.assertEqual('2013-02-13 10:00:00 [UTC+08:00]', entities[0]['value']['timeValue']['instant']['datetime'])
        self.assertEqual('Hour', entities[0]['value']['timeValue']['instant']['grain'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '上两秒'
        text_list = [
            '上二秒',
            '前两秒',
            '前二秒'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('上两秒', entities[0]['body'])
        self.assertEqual('Time', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(3, entities[0]['end'])
        self.assertEqual('2013-02-12 04:29:58 [UTC+08:00]', entities[0]['value']['timeValue']['start']['datetime'])
        self.assertEqual('Second', entities[0]['value']['timeValue']['start']['grain'])
        self.assertEqual('2013-02-12 04:30:00 [UTC+08:00]', entities[0]['value']['timeValue']['end']['datetime'])
        self.assertEqual('Second', entities[0]['value']['timeValue']['end']['grain'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '未来一刻钟'
        text_list = [
            '之后一刻钟',
            '向后一刻钟',
            '往后一刻钟',
            '下一刻钟',
            '后一刻钟'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('未来一刻钟', entities[0]['body'])
        self.assertEqual('Time', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(5, entities[0]['end'])
        self.assertEqual('2013-02-12 04:30:00 [UTC+08:00]', entities[0]['value']['timeValue']['start']['datetime'])
        self.assertEqual('Minute', entities[0]['value']['timeValue']['start']['grain'])
        self.assertEqual('2013-02-12 04:45:00 [UTC+08:00]', entities[0]['value']['timeValue']['end']['datetime'])
        self.assertEqual('Minute', entities[0]['value']['timeValue']['end']['grain'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '星期日'
        text_list = [
            '星期天',
            '礼拜日',
            '礼拜天',
            '周日',
            '周天'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('星期日', entities[0]['body'])
        self.assertEqual('Time', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(3, entities[0]['end'])
        self.assertEqual('2013-02-17 00:00:00 [UTC+08:00]', entities[0]['value']['timeValue']['instant']['datetime'])
        self.assertEqual('Day', entities[0]['value']['timeValue']['instant']['grain'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '这周三'
        text_list = [
            '这礼拜三',
            '今个星期三',
            '今个礼拜三'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('这周三', entities[0]['body'])
        self.assertEqual('Time', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(3, entities[0]['end'])
        self.assertEqual('2013-02-13 00:00:00 [UTC+08:00]', entities[0]['value']['timeValue']['instant']['datetime'])
        self.assertEqual('Day', entities[0]['value']['timeValue']['instant']['grain'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '下周'
        text_list = [
            '下星期',
            '下礼拜'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('下周', entities[0]['body'])
        self.assertEqual('Time', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(2, entities[0]['end'])
        self.assertEqual('2013-02-18 00:00:00 [UTC+08:00]', entities[0]['value']['timeValue']['instant']['datetime'])
        self.assertEqual('Week', entities[0]['value']['timeValue']['instant']['grain'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '三星期后'
        text_list = [
            '三星期之后',
            '三个礼拜后',
            '三个礼拜之后',
            '三星期以后',
            '三星期过后'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('三星期后', entities[0]['body'])
        self.assertEqual('Time', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(4, entities[0]['end'])
        self.assertEqual('2013-03-05 04:30:00 [UTC+08:00]', entities[0]['value']['timeValue']['instant']['datetime'])
        self.assertEqual('Second', entities[0]['value']['timeValue']['instant']['grain'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '国庆节'
        text_list = [
            '十一',
            '国庆'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('国庆节', entities[0]['body'])
        self.assertEqual('Time', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(3, entities[0]['end'])
        self.assertEqual('2013-10-01 00:00:00 [UTC+08:00]', entities[0]['value']['timeValue']['instant']['datetime'])
        self.assertEqual('Day', entities[0]['value']['timeValue']['instant']['grain'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '周一早上'
        text_list = [
            '周一早晨',
            '周一清晨',
            '礼拜一早上',
            '礼拜一早晨',
            '下周一早上'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('周一早上', entities[0]['body'])
        self.assertEqual('Time', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(4, entities[0]['end'])
        self.assertEqual('2013-02-18 04:00:00 [UTC+08:00]', entities[0]['value']['timeValue']['start']['datetime'])
        self.assertEqual('Hour', entities[0]['value']['timeValue']['start']['grain'])
        self.assertEqual('2013-02-18 12:00:00 [UTC+08:00]', entities[0]['value']['timeValue']['end']['datetime'])
        self.assertEqual('Hour', entities[0]['value']['timeValue']['end']['grain'])
        self.assertEqual('早上', entities[0]['value']['partOfDay'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '十月第一个星期一'
        text_list = [
            '十月的第一个星期一'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('十月第一个星期一', entities[0]['body'])
        self.assertEqual('Time', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(8, entities[0]['end'])
        self.assertEqual('2013-10-07 00:00:00 [UTC+08:00]', entities[0]['value']['timeValue']['instant']['datetime'])
        self.assertEqual('Day', entities[0]['value']['timeValue']['instant']['grain'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '女生节下午三点十五'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('女生节下午三点十五', entities[0]['body'])
        self.assertEqual('Time', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(9, entities[0]['end'])
        self.assertEqual('2013-03-07 15:15:00 [UTC+08:00]', entities[0]['value']['timeValue']['instant']['datetime'])
        self.assertEqual('Minute', entities[0]['value']['timeValue']['instant']['grain'])
        self.assertEqual('女生节', entities[0]['value']['holiday'])

        text = '11点05分到15点08分'
        text_list = [
            '11点05到15点08',
            '十一点零五分到十五点零八分',
            '十一点零五到十五点零八',
            '11:05~15:08'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('11点05分到15点08分', entities[0]['body'])
        self.assertEqual('Time', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(13, entities[0]['end'])
        self.assertEqual('2013-02-12 11:05:00 [UTC+08:00]', entities[0]['value']['timeValue']['start']['datetime'])
        self.assertEqual('Minute', entities[0]['value']['timeValue']['start']['grain'])
        self.assertEqual('2013-02-12 15:08:00 [UTC+08:00]', entities[0]['value']['timeValue']['end']['datetime'])
        self.assertEqual('Minute', entities[0]['value']['timeValue']['end']['grain'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '凌晨'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('凌晨', entities[0]['body'])
        self.assertEqual('Time', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(2, entities[0]['end'])
        self.assertEqual('2013-02-12 00:00:00 [UTC+08:00]', entities[0]['value']['timeValue']['start']['datetime'])
        self.assertEqual('Hour', entities[0]['value']['timeValue']['start']['grain'])
        self.assertEqual('2013-02-12 06:00:00 [UTC+08:00]', entities[0]['value']['timeValue']['end']['datetime'])
        self.assertEqual('Hour', entities[0]['value']['timeValue']['end']['grain'])
        self.assertEqual('凌晨', entities[0]['value']['partOfDay'])

        text = '明年的11月份第二个周日'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('明年的11月份第二个周日', entities[0]['body'])
        self.assertEqual('Time', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(12, entities[0]['end'])
        self.assertEqual('2014-11-09 00:00:00 [UTC+08:00]', entities[0]['value']['timeValue']['instant']['datetime'])
        self.assertEqual('Day', entities[0]['value']['timeValue']['instant']['grain'])

        text = '2019年腊月初一上午'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('2019年腊月初一上午', entities[0]['body'])
        self.assertEqual('Time', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(11, entities[0]['end'])
        self.assertEqual('农历 二〇一九年腊月初一 08:00:00 [UTC+08:00]', entities[0]['value']['timeValue']['start']['datetime'])
        self.assertEqual('Hour', entities[0]['value']['timeValue']['start']['grain'])
        self.assertEqual('农历 二〇一九年腊月初一 12:00:00 [UTC+08:00]', entities[0]['value']['timeValue']['end']['datetime'])
        self.assertEqual('Hour', entities[0]['value']['timeValue']['end']['grain'])
        self.assertEqual('上午', entities[0]['value']['partOfDay'])

        text = '下一个中秋节'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('下一个中秋节', entities[0]['body'])
        self.assertEqual('Time', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(6, entities[0]['end'])
        self.assertEqual('农历 二〇一三年八月十五 00:00:00 [UTC+08:00]', entities[0]['value']['timeValue']['instant']['datetime'])
        self.assertEqual('Day', entities[0]['value']['timeValue']['instant']['grain'])
        self.assertEqual('中秋节', entities[0]['value']['holiday'])


if __name__ == '__main__':
    unittest.main()
