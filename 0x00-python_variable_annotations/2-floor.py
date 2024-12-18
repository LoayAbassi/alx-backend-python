#!/usr/bin/env python3
"""contains a floor function"""


def floor(n: float) -> int:
    """returns the largest integer
    less than or equal to n"""
    return int(n) if n >= 0 else int(n)-1
