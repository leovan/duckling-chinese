# -*- coding: utf-8 -*-

from enum import Enum, unique

from com.xiaomi.duckling.ranking import Ranker as JavaRanker


@unique
class DucklingRanker(Enum):
    NAIVE_BAYES = JavaRanker.NaiveBayes


__all__ = [
    'DucklingRanker'
]
