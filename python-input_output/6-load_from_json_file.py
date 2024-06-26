#!/usr/bin/python3
"""
6. Create object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.
    """
    with open(filename, 'r') as jeisan:
        return json.load(jeisan)
