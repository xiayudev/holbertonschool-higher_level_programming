#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        ends = " "
        for i, y in enumerate(x):
            if i == len(x) - 1:
                ends = ""
            print("{:d}".format(y), end=ends)
        print("")
