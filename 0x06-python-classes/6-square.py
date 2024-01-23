#!/usr/bin/python3

"""Define a Square Class"""


class Square:
    """Square Class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization of a new Square.

        Args:
            size (int): The size of the new square.
            position (int, int): pos
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """Get the current position."""
        return self.__position

    @position.setter
    def position(self, value):
        """setting of a new size.

        Args:
            value (int): The value of the new position.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """setting of a new size.

        Args:
            value (int): The value of the new size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size**2

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        for i in range(0, self.__position[1]):
            print("")

        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print("#", end="")
            print("")
