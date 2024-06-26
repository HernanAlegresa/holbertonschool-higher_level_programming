#!/usr/bin/python3
"""
1. Write to a file
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file (UTF8),
    returns the number of characters written.
    """
    with open(filename, "w") as file:
        return file.write(text)
