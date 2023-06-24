#!/usr/bin/python3
"""Module to work with JSON"""


def class_to_json(obj):
    """return the dictionary description of an object

    Args:
        onj (object): Instance of a class

    """
    return obj.__dict__
