#!/usr/bin/env python3
"""
Task 5: Implementing an expiring web cache and tracker
"""
import redis
import requests
from functools import wraps
from typing import Callable


def counter(fn: Callable) -> Callable:
    @wraps(fn)
    def wrapper(url: str) -> str:
        client = redis.Redis()
        client.incr("count:{}".format(url))
        cache_page = client.get("{}".format(url))
        if cache_page:
            return cache_page.decode('utf-8')
        r = fn(url)
        client.set("{}".format(url), r, 10)
        return r
    return wrapper


def get_page(url: str) -> str:
    """
    uses the requests module to obtain
    the HTML content of a particular URL and returns it
    """
    r = requests.get(url)
    return r.text
