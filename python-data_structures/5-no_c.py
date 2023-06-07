#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for c in my_string:
        if ord(c) == 67 or ord(c) == 99:
            continue
        new_str += c
    return new_str
