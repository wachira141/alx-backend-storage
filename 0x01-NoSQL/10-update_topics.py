#!/usr/bin/enc python3
"""
change school topics
"""


def update_topics(mongo_collection, name, topics):
    """
    change all topics of a school doc
    based on the name
    """
    mongo_collection.update_many(
        {'name' : name},
        {'$set' : {'topics' : topics}}
    )
