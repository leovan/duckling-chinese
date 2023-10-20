# -*- coding: utf-8 -*-

import os
import json
import jpype
import jpype.imports
import threading

from pathlib import Path
from datetime import datetime
from typing import *

try:
    from zoneinfo import ZoneInfo
except ImportError:
    from backports.zoneinfo import ZoneInfo


def _start_jvm():
    jvm_options = [
        '-Xms128m',
        '-Xmx2048m',
        '-XX:+IgnoreUnrecognizedVMOptions',
        '--illegal-access=permit',
        '--add-opens=java.base/java.lang=ALL-UNNAMED',
        '--add-opens=java.base/java.util=ALL-UNNAMED',
        '--add-opens=java.base/java.util.regex=ALL-UNNAMED'
    ]

    jars_dir = Path(os.path.dirname(__file__)) / 'jars'

    if not jpype.isJVMStarted():
        jpype.startJVM(
            jpype.getDefaultJVMPath(),
            *jvm_options,
            classpath=[(jars_dir / '*').resolve().as_posix()]
        )


_start_jvm()


import duckling_chinese.dimension as duckling_chinese_dimension
import duckling_chinese.ranker as duckling_chinese_ranker
import duckling_chinese.utils as duckling_chinese_utils

from duckling_chinese.dimension import *
from duckling_chinese.ranker import *
from duckling_chinese.utils import *

from java.lang import Thread as JavaThread
from java.time import ZonedDateTime as JavaZonedDateTime
from java.time import ZoneId as JavaZoneId
from java.time import ZoneOffset as JavaZoneOffset
from java.util import Locale as JavaLocale
from scala import Some as JavaScalaSome
from scala.collection.mutable import HashSet as JavaScalaHashSet
from org.json4s.jackson import Serialization as JavaJsonSerialization

from com.xiaomi.duckling import Api as JavaDucklingApi
from com.xiaomi.duckling import Types as JavaDucklingTypes
from com.xiaomi.duckling.dimension.time import TimeOptions \
    as JavaDucklingTimeOptions
from com.xiaomi.duckling.dimension.numeral import NumeralOptions \
    as JavaDucklingNumeralOptions
from com.xiaomi.duckling import JsonSerde as JavaDucklingJsonSerde


class Duckling(object):
    def __init__(self):
        super(Duckling, self).__init__()

        self._lock = threading.Lock()

        try:
            if threading.active_count() > 1:
                if not JavaThread.isAttached():
                    JavaThread.attach()
            self._lock.acquire()
            self._api = JavaDucklingApi
        finally:
            self._lock.release()

    def gen_context(
            self,
            reference_time=datetime.now(ZoneInfo('Asia/Shanghai')),
            language='zh',
            country='CN'
    ) -> JavaDucklingTypes.Context:

        utc_offset_total_seconds = int(
            reference_time.utcoffset().total_seconds())
        reference_time_java = JavaZonedDateTime.of(
            reference_time.year,
            reference_time.month,
            reference_time.day,
            reference_time.hour,
            reference_time.minute,
            reference_time.second,
            reference_time.microsecond * 1000,
            JavaZoneId.ofOffset(
                'UTC', JavaZoneOffset.ofTotalSeconds(utc_offset_total_seconds))
        )

        locale_java = JavaLocale(language, country)

        return JavaDucklingTypes.Context(reference_time_java, locale_java)

    def gen_rank_options(
            self,
            winner_only=True,
            ranker=DucklingRanker.NAIVE_BAYES,
            combination_rank=True,
            range_rank_ahead=False,
            nodes_limit=800,
            sequence1_end_prune=True
    ) -> JavaDucklingTypes.RankOptions:
        rank_options_java = JavaDucklingTypes.RankOptions()
        rank_options_java.setWinnerOnly(winner_only)
        rank_options_java.setRanker(JavaScalaSome(ranker.value))
        rank_options_java.setCombinationRank(combination_rank)
        rank_options_java.setRangeRankAhead(range_rank_ahead)
        rank_options_java.setNodesLimit(nodes_limit)
        rank_options_java.setSequence1EndsPrune(sequence1_end_prune)

        return rank_options_java

    def gen_time_options(
            self,
            reset_time_of_day=False,
            recent_in_future=True,
            always_in_future=True,
            inherit_grain_of_duration=False,
            parse_four_seasons=False,
            sequence=True,
            duration_fuzzy_on=True,
            duration_fuzzy_value=3,
            before_end_of_interval=False
    ) -> JavaDucklingTimeOptions:
        time_options_java = JavaDucklingTimeOptions()
        time_options_java.setResetTimeOfDay(reset_time_of_day)
        time_options_java.setRecentInFuture(recent_in_future)
        time_options_java.setAlwaysInFuture(always_in_future)
        time_options_java.setInheritGrainOfDuration(inherit_grain_of_duration)
        time_options_java.setParseFourSeasons(parse_four_seasons)
        time_options_java.setSequence(sequence)
        time_options_java.setDurationFuzzyOn(duration_fuzzy_on)
        time_options_java.setDurationFuzzyValue(duration_fuzzy_value)
        time_options_java.setBeforeEndOfInterval(before_end_of_interval)

        return time_options_java

    def gen_numeral_options(
            self,
            allow_zero_leading_digits=False,
            cn_sequence_as_number=False,
            dialect_support=False,
            kmg_support=True
    ) -> JavaDucklingNumeralOptions:
        numeral_options_java = JavaDucklingNumeralOptions()
        numeral_options_java.setAllowZeroLeadingDigits(
            allow_zero_leading_digits)
        numeral_options_java.setCnSequenceAsNumber(cn_sequence_as_number)
        numeral_options_java.setDialectSupport(dialect_support)
        numeral_options_java.setKMG_Support(kmg_support)

        return numeral_options_java

    def gen_options(
            self,
            with_latent=False,
            full=False,
            debug=False,
            targets: Set[DucklingDimension] = None,
            varchar_expand=False,
            entity_with_node=False,
            rank_options: JavaDucklingTypes.RankOptions = None,
            time_options: JavaDucklingTimeOptions = None,
            numeral_options: JavaDucklingNumeralOptions = None
    ) -> JavaDucklingTypes.Options:
        if targets is None:
            targets = list()
        else:
            targets = list(targets)

        targets_java = JavaScalaHashSet()

        for target in targets:
            targets_java.add(target.value)

        targets_java = targets_java.toSet()

        if rank_options is None:
            rank_options = self.gen_rank_options()

        if time_options is None:
            time_options = self.gen_time_options()

        if numeral_options is None:
            numeral_options = self.gen_numeral_options()

        return JavaDucklingTypes.Options(
            with_latent,
            full,
            debug,
            targets_java,
            varchar_expand,
            entity_with_node,
            rank_options,
            time_options,
            numeral_options
        )

    def analyze(
            self,
            text: Text,
            context: JavaDucklingTypes.Context = None,
            options: JavaDucklingTypes.Options = None,
            remove_duplicate=True
    ) -> List[Dict[Text, Any]]:
        if context is None:
            context = self.gen_context()

        if options is None:
            options = self.gen_options()

        answers_java = self._api.analyze(text, context, options)

        if remove_duplicate:
            answers_java = answers_java.distinct()

        answers_json = JavaJsonSerialization.write(
            answers_java,
            JavaDucklingJsonSerde.formats()
        )

        return json.loads(str(answers_json))

    def parse_entities(
            self,
            text: Text,
            context: JavaDucklingTypes.Context = None,
            options: JavaDucklingTypes.Options = None,
            remove_duplicate=True
    ) -> List[Dict[Text, Any]]:
        if context is None:
            context = self.gen_context()

        if options is None:
            options = self.gen_options()

        entities_java = self._api.parseEntities(text, context, options)

        if remove_duplicate:
            entities_java = entities_java.distinct()

        entities_json = JavaJsonSerialization.write(
            entities_java,
            JavaDucklingJsonSerde.formats()
        )

        return json.loads(str(entities_json))


__all__ = [
    'Duckling',
    *duckling_chinese_dimension.__all__,
    *duckling_chinese_ranker.__all__,
    *duckling_chinese_utils.__all__
]


__version__ = '1.1.1'
