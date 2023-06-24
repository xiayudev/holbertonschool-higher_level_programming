#!/usr/bin/python3
"""Module to work with JSON"""


import json


def save_to_json_file(my_obj, filename):
    """Write an Object to a text file

    Args:
        my_obj (object): The object to be transformed
        filename (str): The name of the text file

    """
    with open(filename, mode="w", encoding="utf-8") as f:
        to_json = json.dumps(my_obj)
        f.write(to_json)
