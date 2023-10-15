# -*- coding: utf-8 -*-

from typing import *


def has_same_value(entities: List[Dict], entities_list: List[List[Dict]]):
    for entities_ in entities_list:
        for (first_entity, second_entity) in zip(entities, entities_):
            if first_entity['value'] != second_entity['value']:
                return False

    return True


__all__ = [
    'has_same_value'
]
