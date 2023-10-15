# -*- coding: utf-8 -*-

import unittest

from duckling_chinese.utils import *


class UtilsTestCase(unittest.TestCase):
    def test_lunar_to_solar(self):
        self.assertEqual('一八四九年正月初一', lunar_to_solar('一八四九年正月初一'))
        self.assertEqual('1850-02-12', lunar_to_solar('一八五〇年正月初一'))
        self.assertEqual('2150-12-31', lunar_to_solar('二一五〇年冬月十三'))
        self.assertEqual('二一五一年正月初一', lunar_to_solar('二一五一年正月初一'))

        self.assertEqual('1850-02-12 00:00:00 [UTC+08:00]', lunar_to_solar('农历 一八五〇年正月初一 00:00:00 [UTC+08:00]'))
        self.assertEqual('1850-02-12 00:00:00', lunar_to_solar('农历 一八五〇年正月初一 00:00:00'))
        self.assertEqual('1850-02-12', lunar_to_solar('农历 一八五〇年正月初一'))

        self.assertIsNone(lunar_to_solar(None))
        self.assertEqual('', lunar_to_solar(''))
        self.assertEqual('1850-02-12', lunar_to_solar('1850-02-12'))


if __name__ == '__main__':
    unittest.main()
