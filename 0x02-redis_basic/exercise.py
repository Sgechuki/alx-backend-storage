#!/usr/bin/env python3
"""
Module holds the clas Cache
"""
from functools import wraps
import redis
from typing import Union, Callable, Optional, Any
import uuid


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache():
    """
    store an instance of the Redis client
    as a private variable named _redis
    flush the instance using
    """

    def __init__(self):
        """Initialize"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and
        returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, fn: Optional[Callable[[bytes], Any]] = None) -> Any:
        """convert the data back to the desired format"""
        i = self._redis.get(key)
        if i is None:
            return i
        if fn is not None:
            return fn(i)
        return i

    def get_str(self, key: str) -> Optional[str]:
        """Convert byte to string"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """Convert byte to int"""
        return self.get(key, lambda x: int(x))
