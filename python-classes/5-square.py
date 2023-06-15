#!/usr/bin/python3
"""Create a class named Square"""


class Square:
    """A class with a constructor and an instance attribute size"""

    def __init__(self, size=0):
        """Constructor of the class with one argument

        Args:
            size (int): The size of the square

        """
        self.size = size

    def area(self):
        """Calculate the area of a square

        Returns:
            int: The area of a square

        """
        return self.__size * self.__size

    @property
    def size(self):
        """The getter method that returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """Check size if it is integer

        If size is not integer or it is less than zero raise an exception.

        Args:
            size (int): The size to be checked

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def my_print(self):
        """Prints a square with the character '#' """
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print()
