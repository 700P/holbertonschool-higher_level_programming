#!/usr/bin/python3


def uppercase(str):
    for x in str:
        if chr(97) >= x <= chr(123):
            return(x)
