#!/usr/bin/python3
"""Module to work with a Geometry class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class inherited from BaseGeometry"""

    def __init__(self, width, height):
        """Init method that set height and width"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
