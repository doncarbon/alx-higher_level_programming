#!/usr/bin/python3
"""Defines a Student info class."""


class Student:
    """Student Info Class"""

    def __init__(self, first_name, last_name, age):
        """
        Student Info initialization.

        Args:
            first_name (str): first name.
            last_name (str): last name.
            age (str): age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return self.__dict__
