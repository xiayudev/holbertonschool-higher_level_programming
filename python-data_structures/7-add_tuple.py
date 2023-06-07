#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum_left = 0
    sum_right = 0
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0,
        tuple_a = tuple_a[0], 0
    elif len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0,
        tuple_b = tuple_b[0], 0
    sum_left = tuple_a[0] + tuple_b[0]
    sum_right = tuple_a[1] + tuple_b[1]
    return (sum_left, sum_right)
