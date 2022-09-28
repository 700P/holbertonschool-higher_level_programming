#!/usr/bin/python3
""" return the dictionary description """

def class_to_json(obj):
    """ instance of a class that is serializable """
    return vars(obj)
