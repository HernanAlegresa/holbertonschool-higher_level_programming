#!/usr/bin/python3
"""
Task 10: Square #1
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle.
    """

    def __init__(self, size):
        """Initialize the square with a size."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the square description."""
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
