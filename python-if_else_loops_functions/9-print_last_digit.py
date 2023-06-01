#!/usr/bin/python3
def print_last_digit(number):
    num = repr(number)[-1]
    print(f"{num}", end="")
    return int(num)
