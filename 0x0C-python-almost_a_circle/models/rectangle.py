#!/usr/bin/python3
""" rectangle metrics # 5 is confusing """


from models.base import Base

class Rectangle(Base):
    """ Rectangle Class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Highway connector __init__ """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ area """
        return (self.__width * self.__height)

    def display(self):
        """ print in hashtags """
        print('\n' * self.__y + (' ' * self.__x + '#' * self.__width + '\n') *
              self.__height, end='')

    def validation_of_setters(self, name, value):
        """ (value input) parsing check ie valid value check """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0 and name in ['height', 'width']:
            raise ValueError('{} must be > 0'.format(name))
        if value < 0 and name in ['y', 'x']:
            raise ValueError('{} must be >= 0'.format(name))



    @property
    def width(self):
        """ get attributes of width """
        return self.__width
    
    @width.setter
    def width(self, value):
        """ set attributes of width """
        self.validation_of_setters('width', value)
        self.__width = value

    @property
    def height(self):
        """get attributes of height """
        return self.__height
     
    @height.setter
    def height(self, value):
        """ set attributes of height """
        self.validation_of_setters('height', value)
        self.__height = value

    @property 
    def x(self):
        """get attributes of x """
        return self.__x
    
    @x.setter
    def x(self, value):
        """ set attributes of y """
        self.validation_of_setters('x', value)
        self.__x = value

    @property 
    def y(self):
        """ get attributes of  y """
        return self.__y
    
    @y.setter
    def y(self, value):
        """ set attributes of y """
        self.validation_of_setters('y', value)
        self.__y = value

    def __str__(self):
        """ overide string method """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ assign an argument to each attribute """
        if len(args):
            for iterargs, arg in enumerate(args):
                if iterargs == 0:
                    self.id = arg
                elif iterargs == 1:
                    self.__width = arg
                elif iterargs == 2:
                    self.__height = arg
                elif iterargs == 3:
                    self.__x = arg
                elif iterargs == 4:
                    self.__y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value

    def to_dictionary(self):
        """ dict of rectangle """
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}

