#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mult2 = [True if num % 2 == 0 else False for num in my_list]
    return mult2
