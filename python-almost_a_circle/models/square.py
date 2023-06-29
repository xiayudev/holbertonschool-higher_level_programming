#!/usr/bin/python3
"""Module to work with class Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor with 4 arguments

        Args:
            size (int): The width of the Square
            x (int): Position x
            y (int): Position y
            id (int): The id of the Square

        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Return human readable string"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Getter for the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for validation of size"""
        self.width = value
        self.height = value
