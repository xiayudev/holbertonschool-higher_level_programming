#!/usr/bin/python3
def common_elements(set_1, set_2):
    # For each word in set_1, if set_2 contains this word, add it to the list
    new = [word for word in set_1 if word in set_2]
    return new
