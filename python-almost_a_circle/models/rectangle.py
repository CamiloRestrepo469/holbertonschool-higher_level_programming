#!/usr/bin/python3
"""import class Base"""

from models.base import Base
"""class Rectangle inherited from Base"""


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
        
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if value >= 0:
            self.__height = value
        else:
            raise ValueError("Value must be positive height")
        
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if value >= 0:
            self.__width = value
        else:
            raise ValueError("Value must be positive  with")
        
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value >= 0:
            self.__x = value
        else:
            raise ValueError("Value must be positive x")
        
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        if value >= 0:
            self.__y = value
        else:
            raise ValueError("Value must be positive y")