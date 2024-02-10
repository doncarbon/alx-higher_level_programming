#!/usr/bin/python3
"""
Defines a Square class that's inherited from the Rectangle class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Represents a Square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Rectangle initialization.

        Args:
            size (int): the size of the square.
            x (int): x position of the square.
            y (int): y position of the square.
            id (int): the id attribute of a class.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the Square."""
        square = "[Square] (" + str(self.id)
        square += ") " + str(self.x) + "/" + str(self.y) + " - "
        square += str(self.size)
        return square

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute.

        Args:
            *args (int): arguments to assign to attributes in order.
            **kwargs (int): key-worded arguments to assign to attributes in order.
        """
        arg_list = []
        for arg in args:
            arg_list.append(arg)
        if len(arg_list) != 0:
            for i in range(len(arg_list)):
                if i == 0:
                    self.id = arg_list[i]
                elif i == 1:
                    self.size = arg_list[i]
                elif i == 2:
                    self.x = arg_list[i]
                elif i == 3:
                    self.y = arg_list[i]

        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle.
        """
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
