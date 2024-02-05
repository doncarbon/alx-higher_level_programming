#!/usr/bin/python3
"""Defines a Square class inherited from Rectangle Class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represents a Square Class"""
    def __init__(self, size):
        """
        Initialization of Square class

        Args:
            size (int): size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Return the square area.
        """
        return self.__size * self.__size

    def __str__(self):
        """
            Returns string representation of rectangle.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
