#!/usr/bin/python3
""" Write a function that writes a string  """


def write_file(filename="", text=""):
    """  writes a string to a text file  """
    with open(filename, 'w', encoding='utf-8') as terp:
        return terp.write(text)
