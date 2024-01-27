#!/usr/bin/python3
"""Defines a function that prints \"My name is <first name> <last name>\""""


def say_my_name(first_name, last_name=""):
    """prints \"My name is <first name> <last name>\"

    Args:
        first_name (string): the first name.
        last_name (string): the last name.
    Raises:
        TypeError: If the fist_name isn't a string.
        TypeError: If the last_name isn't a string.
    Returns:
        Nothing.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
