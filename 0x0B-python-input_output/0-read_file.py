#!/usr/bin/python3
"""Defines a read file function."""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): the path to the file.
    """
    with open(filename, 'r', encoding="UTF8") as file:
        print(file.read())
