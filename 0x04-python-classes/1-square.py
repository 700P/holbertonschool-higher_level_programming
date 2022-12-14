#!/usr/bin/python3


"""
question 1

"""


class Square:
    """ size of a square"""
    def __init__(self, size=0):
        """ question 1 """
        if not isinstance(size, int):
                raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
