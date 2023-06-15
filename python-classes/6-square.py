#!/usr/bin/python3
"""Create a class named Square"""


class Square:
    """A class with a constructor and an instance attribute size"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor of the class with one argument

        Args:
            size (int): The size of the square

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """The getter method that returns the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Check if tuple contains 2 integers

        If tuple does not contain 2 integers raise an exception error

        Args:
            value (tuple): The position of the square

        """
        value_1 = isinstance(value[0], int)
        value_2 = isinstance(value[1], int)
        if not value_1 or not value_2 or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            if self.__position[1] > 0:
                for n in range(self.__position[1]):
                    print("")
            for x in range(self.__size):
                for m in range(self.__position[0]):
                    print(" ", end="")
                for y in range(self.__size):
                    print("#", end="")
                print()
