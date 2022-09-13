#!/usr/bin/python3

"""
print a square or raise an error for negative numbers and non integer numbers

"""


def print_square(size):
    """ raise errors for < 0 & float """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        None
    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
