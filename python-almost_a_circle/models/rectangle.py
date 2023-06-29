#!/usr/bin/python3
""" model with class rectangle"""
from models.base import Base


class Rectangle(Base):
    """class rectangle inherits Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """method __init__"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """method getter"""

    @property
    def width(self):
        return self.__width

    """method setter"""

    @width.setter
    def width(self, value):
        self.validaciones("width", value, False)
        self.__width = value

    """method getter"""

    @property
    def height(self):
        return self.__height

    """method setter"""

    @height.setter
    def height(self, value):
        self.validaciones("height", value, False)
        self.__height = value

    """method getter"""

    @property
    def x(self):
        return self.__x

    """method setter"""

    @x.setter
    def x(self, value):
        self.validaciones("x", value)
        self.__x = value

    """method getter"""

    @property
    def y(self):
        return self.__y

    """method setter"""

    @y.setter
    def y(self, value):
        self.validaciones("y", value)
        self.__y = value

    def validaciones(self, name, value, eq=True):
        """validate the value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if eq and value < 0:
            raise ValueError(f"{name} must be >= 0")
        elif not eq and value <= 0:
            raise ValueError(f"{name} must be > 0")

    def area(self):
        """return the area"""
        return self.__width * self.__height

    def display(self):
        """Display the area"""
        print(self.__y * "\n", end="")
        for j in range(self.__height):
            print(str(self.__x * " ") + str(self.__width * "#"))

    def __str__(self):
        """return info about rectangle"""
        id = self.id
        x = self.__x
        y = self.__y
        width = self.__width
        height = self.__height
        return f"[Rectangle] ({id}) {x}/{y} - {width}/{height}"

    def update(self, *args, **kwargs):
        """number of arguments"""
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ["id", "width", "height", "x", "y"]

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    """add dictionary"""

    def to_dictionary(self):
        """create dictionary"""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width,
        }
