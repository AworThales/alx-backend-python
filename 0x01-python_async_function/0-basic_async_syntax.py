#!/usr/bin/env python3
""" My first async program """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """asyncronous program that return a float number
        with a random wait delay
    """

    random_numb = random.uniform(0, max_delay)
    await asyncio.sleep(random_numb)
    return random_numb
