#!/usr/bin/python3
"""Module to work with JSON"""


import json


def to_json_string(my_obj):
    """Return the JSON representation

    Args:
        my_obj (object): The object to be transformed

    """
    return json.dumps(my_obj)
