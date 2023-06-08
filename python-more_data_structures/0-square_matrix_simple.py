#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[num ** 2 for num in matrix[i]] for i in range(len(matrix))]
    return new_matrix
