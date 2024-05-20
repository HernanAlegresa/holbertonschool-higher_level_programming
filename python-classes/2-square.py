#!/usr/bin/python3
'''Defines a class Square.
'''


class Square:
    '''Represents a square.
    '''

    def __init__(self, size=0):
        '''Initialize the square with size
        '''
        self.__size = size
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError('size must be >= 0')
