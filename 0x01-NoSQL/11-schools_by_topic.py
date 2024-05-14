#!/usr/bin/env python3
"""
Task 10: Where can I learn Python?
"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    function that returns the list of school
    having a specific topic
    """
    return mongo_collection.find({"topics": {"$in": [topic]}})
