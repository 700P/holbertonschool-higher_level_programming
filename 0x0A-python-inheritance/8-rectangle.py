#!/usr/bin/python3
"""
Write a class Rectangle
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """ class rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        """ Rectangle that inherits from BaseGeometry """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

