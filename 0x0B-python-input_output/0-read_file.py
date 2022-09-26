#!/usr/bin/python3
""" Write a function that reads a text file (UTF8) and prints it to stdout: """


def read_file(filename=""):
    """ reads a text file """
    with open(filename, 'r', encoding='utf8') as terp:
        print(terp.read(), end='')
