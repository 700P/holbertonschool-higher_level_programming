#!/usr/bin/python3
"""
question 2

"""


class Square:
    """ size of a sqare"""
    def __init__(self, size=0):
        """ question 2 """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ question 2 """
        return self.__size ** 2
