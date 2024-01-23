#!/usr/bin/python3

"""Define a Square Class"""


class Square:
    """Square Class"""

    def __init__(self, size=0):
        """Initialization of a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    def area(self):
        return self.__size**2

    @property
    def size(self):
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

    def my_print(self):
        if self.__size == 0:
            print("")

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
                j += 1
            print("")
            i += 1