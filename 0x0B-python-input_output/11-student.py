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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if attrs is None:
            return self.__dict__

        attrs_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                attrs_dict[attr] = getattr(self, attr)
        return attrs_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance

        Args:
            json (dict): dictionary containing the new attributes.
        """
        for k, v in json.items():
            setattr(self, k, v)
