#!/usr/bin/python3
"""Defines a function that prints a square with the character #."""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): the size of the square.
    Raises:
        TypeError: If the size isn't an integer.
        TypeError: If size is a float and is less than 0.
        ValueError: If size is less than 0.
    Returns:
        Nothing.
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        [print("#", end="") for j in range(size)]
        print("")
