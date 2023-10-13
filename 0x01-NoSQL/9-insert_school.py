#!/usr/bin/env python3
'''9 module
'''


def insert_school(mongo_collection, **kwargs):
    '''Inserts a new document.
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
