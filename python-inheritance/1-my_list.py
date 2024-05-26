#!/usr/bin/python3
"""
Task 1, MyList that inherits from list.
"""


class MyList(list):
    """Class MyList that inherits from list."""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))
