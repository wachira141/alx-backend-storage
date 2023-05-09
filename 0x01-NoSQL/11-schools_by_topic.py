#!/usr/bin/env python3
"""
learn python
"""


def schools_by_topic(mongo_collection, topic):
    """
    func to return the list of school
    having a specific topic
    """
    result = mongo_collection.find({'topics' :{'$elemMatch': {
     '$eq': topic}}});
    return [item for item in result]
