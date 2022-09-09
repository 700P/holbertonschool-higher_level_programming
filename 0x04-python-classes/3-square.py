#!/usr/bin/python3
"""
question 3

"""

class Square:
    """ square with 2 attribute and private property """
    def __init__(self, size=0)
        self.size = size

    def area(self):
        """ question 3 """
        return(self.__size **2)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError(size must be an integer)
        if value < 0:
            raise ValueError(size must be greater than zero)
        self.__size = value
