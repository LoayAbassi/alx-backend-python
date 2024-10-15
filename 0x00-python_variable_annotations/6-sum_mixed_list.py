#!/usr/bin/env python3
"""Write a type-annotated function
sum_mixed_list which takes a list
mxd_ls of integers and floats and
returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_ls: List[Union[int, float]]) -> float:
    """
    returns the sum of elements
    """
    s: float = 0
    for i in mxd_ls:
        s += i
    return s
