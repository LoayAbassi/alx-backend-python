#!/usr/bin/env python3
"""contains a zoom array function"""
from typing import List, Union


def zoom_array(lst: List, factor: Union[int, float] = 2) -> List:
    """

    Args:
        lst (List): list of integers
        factor (Union[int, float], optional): Defaults to 2.

    Returns:
        List: list of new integers 
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
