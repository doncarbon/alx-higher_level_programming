#!/usr/bin/python3
"""Defines a rectangle class that's inherited from BaseGeometry Class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a Rectangle inherited from BaseGeometry"""
    def __init__(self, width, height):
        """
        Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Return the rectangle area.
        """
        return self.__height * self.__width

    def __str__(self):
        """
            Returns string representation of rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
