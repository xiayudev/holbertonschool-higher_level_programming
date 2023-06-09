#!/usr/bin/python3
"""Module to work with class Base
"""


import json
from os.path import exists


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

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square
        rec = None
        if cls is Rectangle:
            rec = Rectangle(4, 5)
        elif cls is Square:
            rec = Square(4)
        rec.update(**dictionary)
        return rec

    @classmethod
    def load_from_file(cls):
        """Return a list of instances"""
        filename = f"{cls.__name__}.json"
        file_exist = exists(filename)
        if file_exist:
            with open(f"{filename}", "r", encoding="utf-8") as f:
                list_objs = cls.from_json_string(f.read())
                return [cls.create(**obj) for obj in list_objs]
        else:
            return []
