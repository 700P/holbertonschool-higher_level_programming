#!/usr/bin/python3
""" returns the list of available attributes and methods """


def lookup(obj):
    """dir func to lookup modules methods"""
    listf = dir(obj)
    return (listf)
