#!/usr/bin/env python3
"""
Main file
"""
import redis
get_page = __import__('web').get_page


url = "http://slowwly.robertomurray.co.uk"
get_page(url)

client = redis.Redis()
print(client.get("count:{}".format(url)))
