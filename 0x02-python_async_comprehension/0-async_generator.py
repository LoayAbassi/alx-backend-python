#!/usr/bin/env python3
"""async generator."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Generate a yielder.
    
    Returns:
        AsyncGenerator[float, None, None]

    Yields:
        Iterator[AsyncGenerator[float, None, None]]
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
