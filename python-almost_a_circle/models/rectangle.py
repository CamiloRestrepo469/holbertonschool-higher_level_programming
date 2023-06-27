#!/usr/bin/python3
"""import class Base"""

from models.base import Base

"""class Rectangle inherited from Base"""


class Rectangle(Base):
    """Base class for Rectangles"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    """getter for the width"""

    @property
    def width(self):
        return self.__width

    """setter for the width"""

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    """getter for the height"""

    @property
    def height(self):
        return self.__height

    """setter for the height"""

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """getter for the x"""

    @property
    def x(self):
        return self.__x

    """setter for the x"""

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """getter for the y"""

    @property
    def y(self):
        return self.__y

    """setter for the y"""

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """method area"""

    def area(self):
        return self.__width * self.__height
