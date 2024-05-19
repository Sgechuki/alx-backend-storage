#!/usr/bin/env python3
"""
Module holds the clas Cache
"""
from functools import wraps
import redis
from typing import Union, Callable, Optional, Any
import uuid


def count_calls(method: Callable) -> Callable:
    """
    Decorator for Cache class methods to track call count
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator for Cache class methods to track input output history
    """
    @wraps(method)
    def wrapper(self, *args):
        key = method.__qualname__
        self._redis.rpush("{}:inputs".format(key), str(args))
        output = method(self, *args)
        self._redis.rpush("{}:outputs".format(key), output)
        return output
    return wrapper


def replay(func: Callable) -> None:
    """
    display the history of calls of a particular function
    """
    client = redis.Redis()
    key = func.__qualname__
    inputs = [i for i in client.lrange("{}:inputs".format(key), 0, -1)]
    outputs = [i for i in client.lrange("{}:outputs".format(key), 0, -1)]
    count = client.get(key).decode('utf-8')
    print("Cache.store was called {} times:".format(count))
    for item in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(key, item[0].decode(
              'utf-8'), item[1].decode('utf-8')))


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
    @call_history
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
