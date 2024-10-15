#!/usr/bin/env python3

"""
Write a type-annotated function sum_list which takes
a list input_list of floats as argument
and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function takes a list of floats as input
    and returns their sum.
    """
    s: float = 0
    for i in input_list:
        s += i
    return s
