#!/usr/bin/python3
"""_summary_
    """


class Rectangle:
    """_summary_
    """

    def __init__(self, width=0, height=0):
        """_summary_

        Args:
            width (int, optional): _description_. Defaults to 0.
            height (int, optional): _description_. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """_summary_

            Args:
                value (_type_): _description_

            Raises:
                TypeError: _description_
                ValueError: _description_
                """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """_summary_

            Args:
                value (_type_): _description_

            Raises:
                TypeError: _description_
                ValueError: _description_
            """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
