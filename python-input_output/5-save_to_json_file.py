#!/usr/bin/python3
"""
5. Save Object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function writes an object to a text file (UTF8) using JSON representation.
    """
    with open(filename, 'w') as filex:
        json.dump(my_obj, filex)
