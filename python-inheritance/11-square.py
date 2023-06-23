#!/usr/bin/python3
"""Module to work with a Square subclass
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class inherited from Rectangle"""

    def __init__(self, size):
        """Init method for Square class"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Human readable output"""
        return f"[Square] {self.__size}/{self.__size}"
