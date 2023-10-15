# -*- coding: utf-8 -*-

from enum import Enum, unique

from com.xiaomi.duckling.dimension import EnumeratedDimension \
    as JavaDucklingEnumeratedDimension


@unique
class DucklingDimension(Enum):
    ACT = JavaDucklingEnumeratedDimension.Act.getDimension()
    AGE = JavaDucklingEnumeratedDimension.Age.getDimension()
    AREA = JavaDucklingEnumeratedDimension.Area.getDimension()
    BLOOD_TYPE = JavaDucklingEnumeratedDimension.BloodType.getDimension()
    CONSTELLATION = JavaDucklingEnumeratedDimension.Constellation.getDimension()
    CURRENCY = JavaDucklingEnumeratedDimension.Currency.getDimension()
    DATE = JavaDucklingEnumeratedDimension.Date.getDimension()
    DIGIT_SEQUENCE = JavaDucklingEnumeratedDimension.DigitSequence.getDimension()
    DISTANCE = JavaDucklingEnumeratedDimension.Distance.getDimension()
    DUPLICATE = JavaDucklingEnumeratedDimension.Duplicate.getDimension()
    DURATION = JavaDucklingEnumeratedDimension.Duration.getDimension()
    EPISODE = JavaDucklingEnumeratedDimension.Episode.getDimension()
    FRACTION = JavaDucklingEnumeratedDimension.Fraction.getDimension()
    GENDER = JavaDucklingEnumeratedDimension.Gender.getDimension()
    LEVEL = JavaDucklingEnumeratedDimension.Level.getDimension()
    LYRIC = JavaDucklingEnumeratedDimension.Lyric.getDimension()
    MULTI_CHAR = JavaDucklingEnumeratedDimension.MultiChar.getDimension()
    MULTIPLE = JavaDucklingEnumeratedDimension.Multiple.getDimension()
    NUMERAL = JavaDucklingEnumeratedDimension.Numeral.getDimension()
    ORDINAL = JavaDucklingEnumeratedDimension.Ordinal.getDimension()
    PHONE_NUMBER = JavaDucklingEnumeratedDimension.PhoneNumber.getDimension()
    PLACE = JavaDucklingEnumeratedDimension.Place.getDimension()
    QUANTITY = JavaDucklingEnumeratedDimension.Quantity.getDimension()
    RATING = JavaDucklingEnumeratedDimension.Rating.getDimension()
    REPEAT = JavaDucklingEnumeratedDimension.Repeat.getDimension()
    SEASON = JavaDucklingEnumeratedDimension.Season.getDimension()
    TEMPERATURE = JavaDucklingEnumeratedDimension.Temperature.getDimension()
    TIME = JavaDucklingEnumeratedDimension.Time.getDimension()
    URL = JavaDucklingEnumeratedDimension.URL.getDimension()
    VELOCITY = JavaDucklingEnumeratedDimension.Velocity.getDimension()


__all__ = [
    'DucklingDimension'
]
