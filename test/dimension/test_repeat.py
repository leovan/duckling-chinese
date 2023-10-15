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


class RepeatTestCase(unittest.TestCase):
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

    def test_repeat(self):
        options = self._duckling.gen_options(
            targets={
                DucklingDimension.REPEAT
            }
        )

        text = '每天'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('每天', entities[0]['body'])
        self.assertEqual('Repeat', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(2, entities[0]['end'])
        self.assertEqual(1, entities[0]['value']['interval']['value'])
        self.assertEqual('Day', entities[0]['value']['interval']['grain'])
        self.assertFalse(entities[0]['value']['interval']['latent'])
        self.assertFalse(entities[0]['value']['interval']['fuzzy'])

        text = '每周'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('每周', entities[0]['body'])
        self.assertEqual('Repeat', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(2, entities[0]['end'])
        self.assertEqual(1, entities[0]['value']['interval']['value'])
        self.assertEqual('Week', entities[0]['value']['interval']['grain'])
        self.assertFalse(entities[0]['value']['interval']['latent'])
        self.assertFalse(entities[0]['value']['interval']['fuzzy'])

        text = '每隔15分钟'
        text_list = [
            '隔15分钟'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('每隔15分钟', entities[0]['body'])
        self.assertEqual('Repeat', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(6, entities[0]['end'])
        self.assertEqual(15, entities[0]['value']['interval']['value'])
        self.assertEqual('Minute', entities[0]['value']['interval']['grain'])
        self.assertFalse(entities[0]['value']['interval']['latent'])
        self.assertFalse(entities[0]['value']['interval']['fuzzy'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '每个月五号的早上'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('每个月五号的早上', entities[0]['body'])
        self.assertEqual('Repeat', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(8, entities[0]['end'])
        self.assertEqual(1, entities[0]['value']['interval']['value'])
        self.assertEqual('Month', entities[0]['value']['interval']['grain'])
        self.assertFalse(entities[0]['value']['interval']['latent'])
        self.assertFalse(entities[0]['value']['interval']['fuzzy'])
        self.assertEqual('2013-03-05 04:00:00 [UTC+08:00]', entities[0]['value']['start']['_1']['timeValue']['start']['datetime'])
        self.assertEqual('Hour', entities[0]['value']['start']['_1']['timeValue']['start']['grain'])
        self.assertEqual('2013-03-05 12:00:00 [UTC+08:00]', entities[0]['value']['start']['_1']['timeValue']['end']['datetime'])
        self.assertEqual('Hour', entities[0]['value']['start']['_1']['timeValue']['end']['grain'])

        text = '每个月的五号'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('每个月的五号', entities[0]['body'])
        self.assertEqual('Repeat', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(6, entities[0]['end'])
        self.assertEqual(1, entities[0]['value']['interval']['value'])
        self.assertEqual('Month', entities[0]['value']['interval']['grain'])
        self.assertFalse(entities[0]['value']['interval']['latent'])
        self.assertFalse(entities[0]['value']['interval']['fuzzy'])
        self.assertEqual('2013-03-05 00:00:00 [UTC+08:00]', entities[0]['value']['start']['_1']['timeValue']['instant']['datetime'])
        self.assertEqual('Day', entities[0]['value']['start']['_1']['timeValue']['instant']['grain'])

        text = '每月2号下午2点'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('每月2号下午2点', entities[0]['body'])
        self.assertEqual('Repeat', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(8, entities[0]['end'])
        self.assertEqual(1, entities[0]['value']['interval']['value'])
        self.assertEqual('Month', entities[0]['value']['interval']['grain'])
        self.assertFalse(entities[0]['value']['interval']['latent'])
        self.assertFalse(entities[0]['value']['interval']['fuzzy'])
        self.assertEqual('2013-03-02 14:00:00 [UTC+08:00]', entities[0]['value']['start']['_1']['timeValue']['instant']['datetime'])
        self.assertEqual('Hour', entities[0]['value']['start']['_1']['timeValue']['instant']['grain'])

        text = '每周三'
        text_list = [
            '每个星期三'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('每周三', entities[0]['body'])
        self.assertEqual('Repeat', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(3, entities[0]['end'])
        self.assertEqual(1, entities[0]['value']['interval']['value'])
        self.assertEqual('Week', entities[0]['value']['interval']['grain'])
        self.assertFalse(entities[0]['value']['interval']['latent'])
        self.assertFalse(entities[0]['value']['interval']['fuzzy'])
        self.assertEqual('2013-02-13 00:00:00 [UTC+08:00]', entities[0]['value']['start']['_1']['timeValue']['instant']['datetime'])
        self.assertEqual('Day', entities[0]['value']['start']['_1']['timeValue']['instant']['grain'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '每天上午八点'
        text_list = [
            '每个上午八点'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('每天上午八点', entities[0]['body'])
        self.assertEqual('Repeat', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(6, entities[0]['end'])
        self.assertEqual(1, entities[0]['value']['interval']['value'])
        self.assertEqual('Day', entities[0]['value']['interval']['grain'])
        self.assertFalse(entities[0]['value']['interval']['latent'])
        self.assertFalse(entities[0]['value']['interval']['fuzzy'])
        self.assertEqual('2013-02-12 08:00:00 [UTC+08:00]', entities[0]['value']['start']['_1']['timeValue']['instant']['datetime'])
        self.assertEqual('Hour', entities[0]['value']['start']['_1']['timeValue']['instant']['grain'])
        self.assertEqual(8, entities[0]['value']['start']['_2']['hours'])
        self.assertFalse(entities[0]['value']['start']['_2']['is12H'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '非工作日'
        text_list = [
            '节假日'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('非工作日', entities[0]['body'])
        self.assertEqual('Repeat', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(4, entities[0]['end'])
        self.assertEqual('NonWorkday', entities[0]['value']['workdayType'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '工作日三点'
        text_list = [
            '每个工作日三点'
        ]
        entities = self._duckling.parse_entities(
            text, self._default_context, options)
        entities_list = [self._duckling.parse_entities(
            text, self._default_context, options) for text in text_list
        ]

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('工作日三点', entities[0]['body'])
        self.assertEqual('Repeat', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(5, entities[0]['end'])
        self.assertEqual('2013-02-13 03:00:00 [UTC+08:00]', entities[0]['value']['start']['_1']['timeValue']['instant']['datetime'])
        self.assertEqual('Hour', entities[0]['value']['start']['_1']['timeValue']['instant']['grain'])
        self.assertEqual(3, entities[0]['value']['start']['_2']['hours'])
        self.assertFalse(entities[0]['value']['start']['_2']['is12H'])
        self.assertEqual('Workday', entities[0]['value']['workdayType'])

        self.assertTrue(has_same_value(entities, entities_list))

        text = '每个工作日上午'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('每个工作日上午', entities[0]['body'])
        self.assertEqual('Repeat', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(7, entities[0]['end'])
        self.assertEqual('2013-02-12 08:00:00 [UTC+08:00]', entities[0]['value']['start']['_1']['timeValue']['start']['datetime'])
        self.assertEqual('Hour', entities[0]['value']['start']['_1']['timeValue']['start']['grain'])
        self.assertEqual('2013-02-12 12:00:00 [UTC+08:00]', entities[0]['value']['start']['_1']['timeValue']['end']['datetime'])
        self.assertEqual('Hour', entities[0]['value']['start']['_1']['timeValue']['end']['grain'])
        self.assertEqual('上午', entities[0]['value']['start']['_1']['partOfDay'])
        self.assertEqual('上午', entities[0]['value']['start']['_2']['part'])
        self.assertEqual('Workday', entities[0]['value']['workdayType'])

        text = '每周三下午'
        entities = self._duckling.parse_entities(
            text, self._default_context, options)

        print(json.dumps(entities, indent=2, ensure_ascii=False))
        self.assertEqual(1, len(entities))
        self.assertEqual('每周三下午', entities[0]['body'])
        self.assertEqual('Repeat', entities[0]['dim'])
        self.assertEqual(0, entities[0]['start'])
        self.assertEqual(5, entities[0]['end'])
        self.assertEqual(1, entities[0]['value']['interval']['value'])
        self.assertEqual('Week', entities[0]['value']['interval']['grain'])
        self.assertFalse(entities[0]['value']['interval']['latent'])
        self.assertFalse(entities[0]['value']['interval']['fuzzy'])
        self.assertEqual('2013-02-13 12:00:00 [UTC+08:00]', entities[0]['value']['start']['_1']['timeValue']['start']['datetime'])
        self.assertEqual('Hour', entities[0]['value']['start']['_1']['timeValue']['start']['grain'])
        self.assertEqual('2013-02-13 18:00:00 [UTC+08:00]', entities[0]['value']['start']['_1']['timeValue']['end']['datetime'])
        self.assertEqual('Hour', entities[0]['value']['start']['_1']['timeValue']['end']['grain'])
        self.assertEqual('下午', entities[0]['value']['start']['_1']['partOfDay'])
        self.assertEqual('下午', entities[0]['value']['start']['_2']['part'])


if __name__ == '__main__':
    unittest.main()
