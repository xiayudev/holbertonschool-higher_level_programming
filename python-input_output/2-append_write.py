#!/usr/bin/python3
"""Module to append a string to a text file"""


def append_write(filename="", text=""):
    """Append strings to a text file

    Args:
        filename (str): The name of the file to append
        text (str): The string to append in filename

    """
    with open(filename, mode="a", encoding="utf-8") as f:
        num_bytes = f.write(text)
        return num_bytes
