#!/usr/bin/python3
""" Write a function that writes """


import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file """
    with open(filename, 'w', encoding='utf-8') as terp:
        json.dump(my_obj, terp)
