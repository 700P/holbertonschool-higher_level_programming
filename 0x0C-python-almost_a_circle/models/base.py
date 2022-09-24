#!/usr/bin/python3
""" Base Class for managaging Id of all other classes/ class instances """

import json
from json import dumps, loads


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
    def from_json_string(json_string):
        """" retrun the json representation of a string list """
        if not json_string or json_string is None:
            return []
        return loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """ class method that returns an instance with all attributes """
        if cls.__name__ == "Rectangle":
            dum_create = cls(4, 5)
        
        elif cls.__name__ == "Square":
            dum_create = cls(6)

        else:
            dum_create = None

        cls.update(dum_create, **dictionary)
        return dum_create

    @classmethod 
    def load_from_file(cls):
        """ return a list of instances """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as JsonFile:
                dir_list = Base.from_json_string(JsonFile.read())
                return [cls.create(**x) for x in dir_list]
        except FileNotFoundError:
            return []
