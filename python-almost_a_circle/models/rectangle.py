#!/usr/bin/python3
"""Module to work with class Rectangle
"""


from models.base import Base


class Rectangle(Base):
    """A class that inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor with 5 arguments

        Args:
            width (int): The width of the Rectangle
            height (int): The height of the Rectangle
            x (int): Position x
            y (int): Position y

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width of the Rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height of the Rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x position"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x position"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y position"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y position"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle"""
        return self.__width * self.__height
