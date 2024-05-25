#!/usr/bin/env python3
"""
Task 5: Implementing an expiring web cache and tracker
"""
import redis
import requests
from functools import wraps
from typing import Callable


client = redis.Redis()


def counter(fn: Callable) -> Callable:
    """
    Counter decorator
    """
    @wraps(fn)
    def wrapper(url: str) -> str:
        client.incr("count:{}".format(url))
        cache_page = client.get("result:{}".format(url))
        if cache_page:
            return cache_page.decode('utf-8')
        r = fn(url)
        client.set("count:{}".format(url), 0)
        client.setex("result:{}".format(url), 10, r)
        return r
    return wrapper


@counter
def get_page(url: str) -> str:
    """
    uses the requests module to obtain
    the HTML content of a particular URL and returns it
    """
    r = requests.get(url)
    return r.text
