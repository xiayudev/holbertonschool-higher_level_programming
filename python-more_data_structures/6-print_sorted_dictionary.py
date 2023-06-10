#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = sorted([k for k in a_dictionary.keys()])  # Get keys and sort them
    for key in new:
        print(f"{key}: {a_dictionary[key]}")
