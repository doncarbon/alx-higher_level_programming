#!/usr/bin/python3
"""
Defines a Base class of all other classes in this current project.
"""


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
