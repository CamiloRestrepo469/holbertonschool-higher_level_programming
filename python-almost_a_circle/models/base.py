#!/usr/bin/python3
"""create a new Base"""


class Base:
    """Base class for"""

    __nb_objects = 0
    """Number of objects"""

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
