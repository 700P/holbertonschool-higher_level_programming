#!/usr/bin/python3
""" Write a class Square that inherits from Rectangle (9-rectangle.py): """

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle """
    def __init__(self, size):
        """ square indentification """
        self.__size = size
        self.integer_validator("size", size)

    def area():
        """ area a the shape """
        return (self.__size ** 2)
