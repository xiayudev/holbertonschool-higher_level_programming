#!/usr/bin/python3
"""Module to work with a Geometry class
"""


class BaseGeometry:
    """A class about a base geometry"""

    def area(self):
        """Computes the area of a geometry"""
        raise Exception("area() is not implemented")
