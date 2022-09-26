#!/usr/bin/python3

"""
raise exception
"""


class BaseGeometry:
    """ raise error with message """
    def area(self):
        raise Exception("area() is not implemented")
