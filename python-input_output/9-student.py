#!/usr/bin/python3
"""Module to work with class Student
"""


class Student:
    """A class that defines attributes and methods for a student"""

    def __init__(self, first_name, last_name, age):
        """Constructor that wakes up with three arguments

        Args:
            first_name (str): The name of the student
            last_name (str): The last name of the student
            age (int): The age of the student

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of a Student instance"""
        return self.__dict__
