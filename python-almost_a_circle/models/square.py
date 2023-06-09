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

    def __str__(self):
        """Return human readable string"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter for the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for validation of size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign attributes according to arguments"""
        if args:
            list_ = ["id", "size", "x", "y"]
            for k, v in zip(list_, args):
                setattr(self, k, v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Return the dictionary representation of a Square"""
        list_ = ["id", "size", "x", "y"]
        return {list_[i]: getattr(self, list_[i])
                for i in range(len(list_)) if hasattr(self, list_[i])}
