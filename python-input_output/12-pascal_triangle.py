#!/usr/bin/python3
"""Module to work with Pascal's triangle (technical interview)
"""


def pascal_triangle(n):
    """Return a bidimensional array of Pascal's triangle"""
    if n <= 0:
        return list()

    array2d = []
    for i in range(n):
        if not array2d:
            array2d.append([1])
        else:
            temp = array2d[len(array2d) - 1][:]
            temp.insert(0, 0)
            temp.append(0)
            list_ = []
            for index, j in enumerate(temp):
                if index < len(temp) - 1:
                    suma = j + temp[index + 1]
                    list_.append(suma)
            array2d.append(list_)
    return array2d
