#!/usr/bin/python3
"""This is a module that contains a function

This function is going to be used to make the project of TDD
"""


def add_integer(a, b=98):
    """Add two integers

    Both of the arguments must be integers or float. Otherwise raise
    an exception. If one of the numbers is type float, convert it to integer.

    Args:
        a (int, float): The first argument
        b (int, float): The second argument to add with a

    Returns:
        The sum of 'a' and 'b'

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    elif type(b) == float:
        b = int(b)

    return a + b
