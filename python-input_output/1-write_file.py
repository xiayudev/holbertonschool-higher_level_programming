#!/usr/bin/python3
"""Module to write a string to a text file"""


def write_file(filename="", text=""):
    """Write strings to a text file

    Args:
        filename (str): The name of the file to write
        text (str): The string to insert in filename

    """
    with open(filename, mode="w", encoding="utf-8") as f:
        num_bytes = f.write(text)
        return num_bytes
