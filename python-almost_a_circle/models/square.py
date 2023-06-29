#!/usr/bin/python3
"""import class Rectangle"""
from models.rectangle import Rectangle


"""Create class"""


class Square(Rectangle):
    """Create constructor"""

    def __init__(self, size, x=0, y=0, id=1):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    """getter"""

    @property
    def size(self):
        return self.width

    """setter"""

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    """method update"""
    def update(self, *args, **kwargs):
        modif_attrs = ['id', 'size', 'x', 'y']

        if args:
            for i, value in enumerate(args[:len(modif_attrs)]):
                setattr(self, modif_attrs[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                if key in modif_attrs:
                    setattr(self, key, value)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

            