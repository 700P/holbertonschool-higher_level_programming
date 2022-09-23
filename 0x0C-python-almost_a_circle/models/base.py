#!/usr/bin/python3
""" Base Class for managaging Id of all other classes/ class instances """

import json


class Base:
    """ Base Class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Highway connector __init__ """
        if id is not None: 
            self.id = id
        else:
             Base.__nb_objects += 1

             self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """ json for transposing data """
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps( list_dictionaries)
        

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to json """
        if list_objs is not None:
            list_objs = [objct.to_dictionary() for objct in list_objs]
        with open("{}.json".format(cls.__name__), "w") as x:
            x.write(cls.to_json_string(list_objs))
    
    @staticmethod
        """ return the list of the json string representation """
        def from_json_string(json_string):


