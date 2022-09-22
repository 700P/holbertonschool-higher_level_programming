#!/usr/bin/python3
""" rectangle metrics """


from models.base import Base

class Rectangle(Base):
    """ Rectangle Class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Highway connector __init__ """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y


