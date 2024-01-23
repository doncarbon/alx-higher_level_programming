#!/usr/bin/python3

"""Define a Square Class"""


class Square:
    """Square Class"""

    def __init__(self, size=0):
        """Initialization of a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
