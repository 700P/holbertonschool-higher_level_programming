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
        

            

# private instance base.__no_objects
#                   ^   ^ 
# public instance 'self.id'
#                  ^   ^
