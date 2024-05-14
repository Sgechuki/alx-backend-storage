#!/usr/bin/env python3
"""
Task 8: List all documents in Python
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    lists all documents in a collection
    Return an empty list if no document in the collection
    """
    return [doc for doc in mongo_collection.find()]
