#!/usr/bin/python3
"""Full rectangle"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Write a class Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        """ indentify Rectangle class """
        self.__width = width
        self.__height = height
        self.integer_validator = ("width", width)
        self.integer_validator = ("height", height)

    def __repr__(self):
        """ return the area() method must be implemented """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ return the area of a rectangle """
        return self.__width * self.__height
