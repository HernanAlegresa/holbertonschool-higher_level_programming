#!/usr/bin/python3
"""
2. Append to a file
"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file (UTF8),
    returns the number of characters added.
    """
    with open(filename, "a") as fail:
        return fail.write(text)
