#!/usr/bin/env python3
""" list annotation """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes mixed number type and return float
    """
    return sum(mxd_lst)
