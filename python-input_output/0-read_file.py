#!/usr/bin/python3
"""
0. Read file
"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout.
    """
    with open(filename, "r") as failneim:
        print(failneim.read(), end="")
