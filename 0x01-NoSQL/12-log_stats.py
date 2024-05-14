#!/usr/bin/env python3
"""
Task 12: Log stats
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs.nginx

    logs_count = db.count_documents({})
    print("{} logs".format(logs_count))

    get = db.count_documents({'method': 'GET'})
    post = db.count_documents({'method': 'POST'})
    put = db.count_documents({'method': 'PUT'})
    patch = db.count_documents({'method': 'PATCH'})
    delete = db.count_documents({'method': 'DELETE'})

    print("Methods:")
    print("\tmethod GET: {}".format(get))
    print("\tmethod POST: {}".format(post))
    print("\tmethod PUT: {}".format(put))
    print("\tmethod PATCH: {}".format(patch))
    print("\tmethod DELETE: {}".format(delete))

    status = db.count_documents({'method': 'GET', 'path': '/status'})
    print("{} status check".format(status))
