#!/usr/bin/python3
"""sorted list ascending"""


class MyList(list):
    """ subclass of List """
    def print_sorted(self):
        """prints the list ascend"""
        print(sorted(self))
