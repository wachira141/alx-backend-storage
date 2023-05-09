#!/usr/bin/env python3
"""
list all documents in a collection
"""


def list_all(mongo_collection):
    """
    func to list all collections
    """
    return [item for item in mongo_collection.find()]
