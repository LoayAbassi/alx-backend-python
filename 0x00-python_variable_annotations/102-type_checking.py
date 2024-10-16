#!/usr/bin/env python3
"""contains a zoom array function"""
from typing import List, Union, Tuple


def zoom_array(lst: Tuple, factor: Union[int, float] = 2) -> List:
    """
    Args:
        lst (Tuple): tuple of integers
        factor (Union[int, float], optional): Defaults to 2.

    Returns:
        List: list of new integers 
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)  # Define array as a tuple

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
