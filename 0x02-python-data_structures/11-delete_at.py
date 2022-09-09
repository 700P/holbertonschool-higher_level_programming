#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
     if 0 > idx >= len(my_list):
         return my_list
     try:
         del my_list[idx]
     except:
         pass
     return my_list
