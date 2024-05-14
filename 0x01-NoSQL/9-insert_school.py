#!/usr/bin/env python3
"""
Task 8: Insert a document in Python
"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs
    Return the new _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
