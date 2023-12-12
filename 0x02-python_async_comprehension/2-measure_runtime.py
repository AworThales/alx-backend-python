#!/usr/bin/env python3
""" 2. Run time for four parallel comprehensions
"""

import asyncio
from time import perf_counter
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Run in parallel
    """
    g = perf_counter()
    my_task = [asyncio.create_task(async_comprehension()) for x in range(4)]
    await asyncio.gather(*my_task)
    elapsed = perf_counter() - g
    return elapsed
