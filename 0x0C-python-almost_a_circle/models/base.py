#!/usr/bin/python3
""" Base Class for managaging Id of all other classes/ class instances"""


class Base:
    """ Base Clase """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Highway connector __init__ """
        if id is not None: 
            self.id = id
        else:
             Base.__nb_objects += 1

             self.id = self.__nb_objects


            

# private instance base.__no_objects
#                   ^   ^ 
# public instance 'self.id'
#                  ^   ^
