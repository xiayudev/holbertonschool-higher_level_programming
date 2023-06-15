#!/usr/bin/python3
"""Create a class named Square"""


class Square:
    """A class with a constructor and an instance attribute size"""

    def __init__(self, size=0):
        """Constructor of the class with one argument

        Check if size is integer, if so raise an exception error.

        Args:
            size (int): The size of the square

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
