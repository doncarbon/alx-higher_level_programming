#!/usr/bin/python3
"""Defines an BaseGeometry Class."""


class BaseGeometry:
    """BaseGeometry class."""
    def __init__(self):
        """Empty initialization"""
        pass

    def area(self):
        """Area method (still not implemented)"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Value validator

        Args:
            name (str): the name of value.
            value (int): value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
