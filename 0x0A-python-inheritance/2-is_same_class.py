#!/usr/bin/python3
"""Defines a function that checks if the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance of the specified class

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If the object is exactly an instance of the specified class - True
        Otherwise - False"""
    if type(obj) == a_class:
        return True
    return False
