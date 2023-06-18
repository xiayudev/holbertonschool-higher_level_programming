#!/usr/bin/python3
"""Module to work with a rectangle

Working with a class called rectangle to print it with
a given height and width.

"""


class Rectangle:
    """A class with a constructor, getters and setters"""

    def __init__(self, width=0, height=0):
        """Constructor with two arguments

        Set the height and with of the rectangle

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """The getter method that returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """The setter method that checks for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The getter method that returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """The setter method that checks for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Computes the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """The dunder str for human readable representation"""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            for i in range(self.__height):
                print("#" * self.__width, end="")
                if i == self.__height - 1:
                    print("", end="")
                else:
                    print()
            return f""

    def __repr__(self):
        """The dunder repr for debugging purposes"""
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

    def __del__(self):
        """For Destroying an instance"""
        print("Bye rectangle...")
