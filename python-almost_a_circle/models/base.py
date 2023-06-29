#!/usr/bin/python3
"""Module to work with class Base
"""


import json


class Base:
    """A class that serves as a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor with just one argument

        Args:
            id (int): The id of the class

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return a JSON string representation"""
        if list_dictionaries is None or not list_dictionaries:
            return '"[]"'
        else:
            return json.dumps(list_dictionaries)
