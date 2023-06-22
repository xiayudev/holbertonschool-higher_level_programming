#!/usr/bin/python3
"""Module to check an object
"""


def inherits_from(obj, a_class):
    """Return True if an object is an instance of a class"""
    return type(obj) != a_class
