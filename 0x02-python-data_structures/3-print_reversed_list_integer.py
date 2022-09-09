#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    mylist = reversed(my_list)
    for x in mylist:
        print("{:d}".format(x))
