#!/usr/bin/python3
""" My class module
"""

class MyClass:
    """ My class """

    def __init__(self, name):
        """ returns the dictionary description """ 
        self.name = name
        self.number = 0

    def __str__(self):
        """ JSON serialization of an object: """
        return "[MyClass] {} - {:d}".format(self.name, self.number)
