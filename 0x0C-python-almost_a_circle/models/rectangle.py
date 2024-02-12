#!/usr/bin/python3
"""
Defines a Rectangle class that's inherited from the Base class.
"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a Rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        a new Rectangle initialization.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
            x (int): x position.
            y (int): y position.
            id (int): the id attribute of a class.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    @property
    def width(self):
        """Get/set the current width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        setting of a new width.

        Args:
            value (int): The value of the new width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the current height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        setting of a new height.

        Args:
            value (int): The value of the new height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get/set the current x pos of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        setting of a new x.

        Args:
            value (int): The value of the new x pos of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get/set the current y pos of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """setting of a new y.

        Args:
            value (int): The value of the new y pos of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the current area of the rectangle."""
        return self.height * self.width

    def display(self, *args):
        """
        Prints in stdout the Rectangle instance with the character #.
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print() for pos in range(self.__y)]
        for i in range(0, self.__height):
            print(self.__x * " ", end="")
            [print("#", end="") for j in range(self.__width)]
            print()

    def __str__(self):
        """Return the string representation of the Rectangle."""
        rect = "[Rectangle] (" + str(self.id)
        rect += ") " + str(self.__x) + "/" + str(self.__y) + " - "
        rect += str(self.__width) + "/" + str(self.__height)
        return rect

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        arg_list = []
        for arg in args:
            arg_list.append(arg)
        if len(arg_list) != 0:
            for i in range(len(arg_list)):
                if i == 0:
                    if arg_list[i] is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        Rectangle.id = arg_list[i]
                elif i == 1:
                    self.width = arg_list[i]
                elif i == 2:
                    self.height = arg_list[i]
                elif i == 3:
                    self.x = arg_list[i]
                elif i == 4:
                    self.y = arg_list[i]

        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle.
        """
        return {"x": self.x, "y": self.y, "id": self.id, "height": self.height, "width": self.width}
