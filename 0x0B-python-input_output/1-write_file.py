#!/usr/bin/python3
"""Defines a writing to file function."""


def write_file(filename="", text=""):
    """
    Writes a text to filename and returns the number of chars written.

    Args:
        filename (str): the path to the file.
        text (str): text to write.

    Returns:
        the number of chars written.
    """
    with open(filename, 'w', encoding="UTF8") as file:
        chars = file.write(text)

    return chars
