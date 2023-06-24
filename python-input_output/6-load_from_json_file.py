#!/usr/bin/python3
"""Module to work with JSON"""


import json


def load_from_json_file(filename):
    """Create an object from JSON file

    Args:
        filename (str): The name of the text file

    """
    with open(filename, mode="r", encoding="utf-8") as f:
        to_object = json.load(f)
        return to_object
