#!/usr/bin/python3
"""Module to work with a Geometry class
"""


class BaseGeometry:
    """A class about a base geometry"""

    def area(self):
        """Computes the area of a geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer containing in value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A class inherited from BaseGeometry"""

    def __init__(self, width, height):
        """Init method that set height and widht"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
