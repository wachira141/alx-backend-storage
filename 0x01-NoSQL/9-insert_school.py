#!/usr/bin/env python3
"""
insert a document in python
"""


def insert_school(mongo_collection, **kwargs):
    """
    insert new doc in a collection
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
