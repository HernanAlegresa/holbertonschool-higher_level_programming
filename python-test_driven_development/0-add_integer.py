#!/usr/bin/python3
"""
This module function, adds 2 integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Args:
        a: int or float.
        b: int or float ,defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
