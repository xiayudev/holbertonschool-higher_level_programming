#!/usr/bin/python3
"""Create a class named Square"""


class Square:
    """A class with a constructor and an instance attribute size"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor of the class with one argument

        Args:
            size (int): The size of the square
            position (tuple): The coordinates if the square

        """
        self.size = size
        self.position = position

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
        val_1 = isinstance(value[0], int)
        val_2 = isinstance(value[1], int)
        if not val_1 or not val_2 or len(value) != 2 or type(value) != tuple \
                or not value[0] >= 0 or not value[1] >= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @size.setter
    def size(self, value):
        """Check size if it is integer

        If size is not integer or it is less than zero raise an exception.

        Args:
            value (int): The size to be checked

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of a square

        Returns:
            int: The area of a square

        """
        return self.__size * self.__size

    def my_print(self):
        """Prints a square with the character '#' """
        if self.size == 0:
            print()
        else:
            if self.position[1] > 0:
                for n in range(self.position[1]):
                    print()
            for x in range(self.size):
                for m in range(self.position[0]):
                    print(" ", end="")
                for y in range(self.size):
                    print("#", end="")
                print()
