#!/usr/bin/python3
"""
8. Class to JSON
"""


def class_to_json(obj):
    """
    Function returns the dictionary description with simple data structure,
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object.
    """
    return obj.__dict__
