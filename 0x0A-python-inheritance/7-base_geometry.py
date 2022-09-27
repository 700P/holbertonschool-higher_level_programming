#!/usr/bin/python3
"""
integer validator
"""


class BaseGeometry():
    """ class name """
    def area(self):
        """ raise error with message """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validates value: """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
