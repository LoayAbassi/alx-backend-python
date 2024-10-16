#!/usr/bin/env python3
"""contains a zoom array function"""
from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Args:
        lst (Tuple[int, ...]): tuple of integers
        factor (int, optional): Defaults to 2.

    Returns:
        List[int]: list of new integers 
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)  # Define array as a tuple

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
