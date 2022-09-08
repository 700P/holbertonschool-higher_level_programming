#!/usr/bin/python3


class Square:
    def __init__(self, size=0)
        self.size = size

    def area(self):
        return(self.__size **2)

    def area(self):
        if self.__size == 0:
            print()
        else:
            for a in range(self.__size):
                for b in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError(size must be an integer)
        if value < 0:
            raise ValueError(size must be greater than zero)
        self.__size = value