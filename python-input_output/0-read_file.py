#!/usr/bin/python3
"""Module to read a file"""


def read_file(filename=""):
    """Read the entire file using with keyword

    Args:
        filename (str): The name of the file to read

    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
