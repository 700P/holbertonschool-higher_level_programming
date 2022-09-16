#!/usr/bin/python3


"""
inherit class
"""

def inherits_from(obj, a_class):
    if obj.__class__ is a_class:
        return False
    return issublcass(obj.__class__, a_class)
