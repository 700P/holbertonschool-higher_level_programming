#!/usr/bin/python3
""" square class """


from models.rectangle import Rectangle

class Square(Rectangle):
    """ inherit the Rectanle attributes """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = size
        self.__width = size
        self.__height = size

    def __str__(self, **kwargs):
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


    def update(self, *args, **kwargs):
        """ update the square attribute """
        if len(args):
            """args non-kwargs"""
            for iterarg, arg in enumerate(args):
                if iterarg == 0:
                    self.id = arg
                elif iterarg == 1:
                    self.size = arg
                elif iterarg == 2:
                    self.x = arg
                elif iterarg == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
