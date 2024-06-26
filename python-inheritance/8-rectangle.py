#!/usr/bin/python3
"""
Task 8: Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """Initialize the rectangle with width and height."""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
