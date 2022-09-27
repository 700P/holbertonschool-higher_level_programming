#!/usr/bin/python3
"""
Full rectangle
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry
BaseGeometry = __import__("8-rectangle").BaseGeometry

class Rectangle(BaseGeometry):
    """ Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py) """
    def __init__(self, width, height):
        self.__width = width
        self.__heigt = height
        self.integer_validator = ("width", width)
        self.integer_validator = ("height", height)
    
    def __repr__(self):
        """ return the area() method must be implemented """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ return the area of a rectangle """
        return self.__width * self.__height
