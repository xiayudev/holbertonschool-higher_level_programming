#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        big_value = -9999
        key = ""
        for k, val in a_dictionary.items():
            if val > big_value:
                big_value = val
                key = k
        if big_value:
            return key
