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
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string to a file"""
        if list_objs is None:
            with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
                f.write(cls.to_json_string([]))
        else:
            with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
                list_temp = [cls.to_dictionary(obj) for obj in list_objs]
                f.write(cls.to_json_string(list_temp))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON representation json_string"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)
