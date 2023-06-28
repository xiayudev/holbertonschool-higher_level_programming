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
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        pass

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        pass

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        pass

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        pass
