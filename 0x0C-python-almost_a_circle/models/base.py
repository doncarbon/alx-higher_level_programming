#!/usr/bin/python3
"""
Defines a Base class of all other classes in this current project.
"""
import json


class Base:
    """
    Manage id attribute in all your future classes and avoid
    duplicating the same code (by extension, same bugs).
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor (initialization)

        Args:
            id (int): the id attribute of a class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (dict): the dict to convert.

        Return:
            the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of objects.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="UTF8") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): JSON string representation.

        Return:
            the list of the JSON string representation json_string.
        """
        if json_string is None or len(json_string) == 0:
            return "[]"

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            dictionary (dict): a double pointer to a dictionary.

        Return:
            An instance with all attributes already set.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                cname = cls(1, 1)
            else:
                cname = cls(1)
        cname.update(**dictionary)
        return cname
