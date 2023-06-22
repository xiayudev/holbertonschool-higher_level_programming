#!/usr/bin/python3
"""Module to inherit from list object
"""


class MyList(list):
    """Class that inherits from list superclass"""

    def print_sorted(self):
        """Print all items in list"""
        print(f"{sorted(self)}")
