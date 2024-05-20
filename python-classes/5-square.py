#!/usr/bin/python3
'''Defines a class Square that defines a square with size, calculates area, and can print the square.
'''


class Square:
    '''Represents a square.
    '''
    
    def __init__(self, size=0):
        '''Initialize the square with size
        '''
        self.size = size

    @property
    def size(self):
        '''Get the size of the square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''Set the size of the square and validate it
        '''
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Defines the area of a square
        '''
        return self.__size * self.__size

    def my_print(self):
        '''Prints the square with the character #
        '''
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
