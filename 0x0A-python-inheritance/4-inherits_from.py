#!/usr/bin/python3
"""
inherit class
"""

def inherits_from(obj, a_class):
    """  if the object is an instance of a class that inherited (directly or indirectly) from the specified class """
    if obj.__class__ is a_class:
        return False
    return issublcass(obj.__class__, a_class)
