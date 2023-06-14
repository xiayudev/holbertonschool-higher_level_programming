#!/usr/bin/python3
"""Create a class named Square"""


class Square:
    """A class with a constructor and an instance attribute size"""

    def __init__(self, size):
        """Constructor of the class with one argument

        Args:
            size (int): The size of the square

        """
        self.__size = size
