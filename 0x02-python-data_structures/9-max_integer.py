#!/usr/bin/python3


def max_integer(my_list=[]):
    maxnum = None
    if not my_list:
        return None
    for x in my_list:
        if maxnum is None or x > maxnum:
            maxnum = x
    return maxnum
