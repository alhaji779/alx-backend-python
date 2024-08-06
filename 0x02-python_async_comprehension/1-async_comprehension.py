#!/usr/bin/env python3
""" async list comprehension task2"""
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Async list comprehension function
    """
    return [n async for n in async_generator()]
