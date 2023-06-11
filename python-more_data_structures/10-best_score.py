#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        big_value = a_dictionary[list(a_dictionary)[0]]  # Get the first value
        key = ""
        for k, val in a_dictionary.items():
            if val > big_value:
                big_value = val
                key = k
        return key
