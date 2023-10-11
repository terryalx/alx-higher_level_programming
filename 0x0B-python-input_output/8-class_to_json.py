#!/usr/bin/python3

"""
Write a function that returns the dictionary description 
with simple data structure 
(list, dictionary, string, integer and boolean) 
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    args:
        obj: is an instance of a Class
        All attributes of the obj Class are serializable:
    """

    return obj.__dict__
