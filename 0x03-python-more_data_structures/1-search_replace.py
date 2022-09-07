#!/usr/bin/bash


def search_replace(my_list, search, replace):
    return list(map(lambda a: a if a != search else replace, my_list))
