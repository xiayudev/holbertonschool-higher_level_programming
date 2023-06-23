#!/usr/bin/python3
"""Module to work with a Square subclass
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class inherited from Rectangle"""

    def __init__(self, size):
        """Init method for Square class"""
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size
