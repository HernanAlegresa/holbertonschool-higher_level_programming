#!/usr/bin/python3
'''Defines an empty class Square that defines a square.
'''


class Square:
    '''Represents a square.
    '''
    
    def __init__(self, size=0):
        '''Initialize the square with size
        '''
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError('size must be >= 0')
