#!/usr/bin/python3
"""Defines an appending text to file function."""


def append_write(filename="", text=""):
    """
    Appends a text to filename's EOF and returns the number of chars added.

    Args:
        filename (str): the path to the file.
        text (str): text to append.

    Returns:
        the number of chars added.
    """
    with open(filename, 'a', encoding="UTF8") as file:
        chars = file.write(text)

    return chars
