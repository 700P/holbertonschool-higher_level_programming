#!/usr/bin/python3
""" Write a function that creates an Object from a “JSON file”: """


import json

def load_from_json_file(filename):
    """ create an Object from a “JSON file """
    with open(filename, 'r', encoding='utf=8') as terp:
        return json.loads(terp.read())
