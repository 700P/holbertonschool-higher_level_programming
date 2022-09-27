#!/usr/bin/python3
"""
sorted list ascending
"""

class MyList(list):
    """ print parent (list) """
    def print_sorted(self):
        print(sorted(self))

