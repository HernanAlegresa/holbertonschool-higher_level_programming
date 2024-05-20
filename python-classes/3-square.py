#!/usr/bin/python3
"""An empty class 'Square' that defines a square"""
class Square:
    """The square"""
    def __init__(self, size=0):
        """Initialize the square with size"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Defines the area of a square"""
        return self.__size * self.__size
