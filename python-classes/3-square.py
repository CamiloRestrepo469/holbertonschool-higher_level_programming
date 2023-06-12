#!/usr/bin/python3
"""create a class that Square"""
class Square:
    """ create instance of Square"""
    def __init__(self, size=0):
        """Initialize a new square.

    Args:
        size (int): The size of the new square.
    """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
