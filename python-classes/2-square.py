#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.set_size(size)

    def get_size(self):
        """Get the size of the square."""
        return self.__size

    def set_size(self, size):
        """Set the size of the square.

        Args:
            size (int): The new size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
