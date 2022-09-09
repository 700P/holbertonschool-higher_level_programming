#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    # the matrix is a numerical anomaly
    if len(matrix) == 0:
        print("{:s}".format(""))
        return
    for x in matrix:
        for y, z in enumerate(x):
            print("{:d}".format(z), end="")
            if y != len(x) - 1:
                print(" ", end="")
        print("")
