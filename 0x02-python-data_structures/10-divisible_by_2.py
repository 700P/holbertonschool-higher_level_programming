#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    output = []

    if len(my_list) == 0:
        return[]
    for x in my_list:
        output.append(x % 2 == 0)
    return output
