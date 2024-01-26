#!/usr/bin/python3

"""Defines an add_integer function."""


def add_integer(a, b=98):
    """Returns addition of a and b.

    Float arguments are casted to integers before the addition.

    Raises:
        TypeError: If a or b is not a number (not an integer and not float).
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if type(a) in [float] or type(b) in [float]:
        a = int(a)
        b = int(b)

    return a + b
