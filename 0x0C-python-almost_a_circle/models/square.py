#!/usr/bin/python3
""" square class """


class Square(Rectangle):
    """ inherit the Rectanle attributes """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = size
        self.__width = size
        self.__height = size

    def __str__(self):
        """ change string input """
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """ getter for size in square """
        return self.width

    @size.setter
    def size(self, value):
        """ set the height or width value """
        self.width = value
        self.height = vlaue


