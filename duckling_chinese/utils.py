# -*- coding: utf-8 -*-

import os

from typing import *
from pathlib import Path
from zipfile import ZipFile
from io import TextIOWrapper


def _build_solar_lunar_mapping(revert=False) -> Dict[Text, Text]:
    lunar_jar_path = Path(os.path.dirname(__file__)) / 'jars' / 'lunar-1.5.jar'

    mapping = {}

    with ZipFile(lunar_jar_path, 'r') as z:
        with TextIOWrapper(z.open('solar2lunar.txt', 'r'), encoding='utf-8') as f:
            lines = f.readlines()

            for line in lines:
                line_parts = line.split(' <====> ')
                if len(line_parts) != 2:
                    continue

                solar_date = line_parts[0]
                lunar_date_info = line_parts[1]

                lunar_date_info_parts = lunar_date_info.split(' ')
                if len(lunar_date_info_parts) != 3:
                    continue

                lunar_date = lunar_date_info_parts[0]

                if not revert:
                    mapping[solar_date] = lunar_date
                else:
                    mapping[lunar_date] = solar_date

    return mapping


_LUNAR_SOLAR = _build_solar_lunar_mapping(revert=True)


def _lunar_date_to_solar_date(lunar_date: Text) -> Text:
    return _LUNAR_SOLAR.get(lunar_date, lunar_date)


def lunar_to_solar(lunar_datetime: Optional[Text]) -> Optional[Text]:
    if lunar_datetime is None:
        return None

    tmp_datetime = lunar_datetime.replace('农历', '').strip()
    tmp_datetime_parts = tmp_datetime.split(' ')
    lunar_date = tmp_datetime_parts[0]

    if len(tmp_datetime_parts) <= 1:
        tmp_time = ''
    else:
        tmp_time = ' ' + ' '.join(tmp_datetime_parts[1:])

    solar_date = _lunar_date_to_solar_date(lunar_date)

    return solar_date + tmp_time


__all__ = [
    'lunar_to_solar'
]
