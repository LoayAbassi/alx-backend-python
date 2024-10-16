#!/usr/bin/env python3

"""contains a wait_n function"""

import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """returns a sorted list of n delays"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    done = []
    # awaiting all tasks
    for completed in asyncio.as_completed(tasks) :
        res = await completed
        done.append(res)

    return done
