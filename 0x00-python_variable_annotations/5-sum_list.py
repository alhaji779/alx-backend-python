#!/usr/bin/env python3
""" list type variable definition """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ function that sums up a lis
    """
    new_list = sum(input_list)
    return new_list
