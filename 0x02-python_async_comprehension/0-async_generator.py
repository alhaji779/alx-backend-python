#!/usr/bin/env python3
""" Ascnc comprehension task1 """
import asyncio
import random


async def async_generator():
    """ Async genetaror method
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
