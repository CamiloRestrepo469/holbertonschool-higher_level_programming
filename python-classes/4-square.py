#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.
        """
        if not isinstance(value, int):
            """si not of type int raises TypeError"""
            raise TypeError("size must be an integer")
        elif value < 0:
            """de lo contrario raise valueError"""
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Get the area of the square

     returns the area of the square
       """
        return self.__size**2
