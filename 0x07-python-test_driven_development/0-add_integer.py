#!/usr/bin/python3

"""
raise an integer error for add inter method
"""


def add_integer(a, b=98):
    """ add casted integer """
    if type(x) != int or type(x) == float:
            x = int(x)
    else:
        raise TypeError("x must be an integer")
    if type(y) != int or type(y) == float:
        y == int(y)
    else:
        raise TypeError("y must be and integer")
    return (x + y)
