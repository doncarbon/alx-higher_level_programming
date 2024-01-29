#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Rectangle Class

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol for string representation.
        """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization of a new Square.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height

    def __del__(self):
        """Prints Bye rectangle when an instance gets deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Get/set the current width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """setting of a new width.

        Args:
            value (int): The value of the new width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the current height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """setting of a new height.

        Args:
            value (int): The value of the new height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the current area of the rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Return the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """Print the rectangle with the character #."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = []
        for i in range(self.__height):
            [rectangle.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return "".join(rectangle)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return rectangle
