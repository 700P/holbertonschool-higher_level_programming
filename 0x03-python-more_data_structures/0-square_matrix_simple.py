#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    return list(map(lambda b: list(map(lambda a: a**2, b)), matrix))
