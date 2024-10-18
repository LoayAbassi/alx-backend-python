#!/usr/bin/env python3
"""
returning a list with random values.
"""

from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Async comprehension generator.
    """
    return [i async for i in async_generator()]
