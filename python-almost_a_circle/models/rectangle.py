#!/usr/bin/python3
"""import class Base"""

from models.base import Base

"""class Rectangle inherited from Base"""


class Rectangle(Base):
    """Base class for Rectangles"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        

    """getter width"""

    @property
    def width(self):
        return self.__width

    """setter width"""

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    """getter height"""

    @property
    def height(self):
        return self.__height

    """setter height"""

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """getter x"""

    @property
    def x(self):
        return self.__x

    """setter x"""

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """getter y"""

    @property
    def y(self):
        return self.__y

    """setter y"""

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """add area to the Rectangle"""

    def area(self):
        return self.__width * self.__height
    
    """add method public"""
    def display(self):
        for i in range(self.__height):
            print("#" * self.__width)
