#!/usr/bin/en python3
"""
contains task_wait_n function
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n (int)
        max_delay (int)

    Returns:
        List[float]
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    done = []
    # awaiting all tasks
    for completed in asyncio.as_completed(tasks):
        res = await completed
        done.append(res)

    return done
