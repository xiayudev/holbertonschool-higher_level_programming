#!/usr/bin/python3
"""Module to work with JSON"""


import json


def from_json_string(my_str):
    """Return the object from JSON

    Args:
        my_str (str): The string to be transformed

    """
    return json.loads(my_str)
