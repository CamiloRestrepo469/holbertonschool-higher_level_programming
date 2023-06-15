#!/usr/bin/python3
"""
Define print # in multiple lines
"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif not isinstance(size, int) or size < 0:
        raise ValueError('size must be >= 0')
    elif not isinstance(size, float) and size < 0:
        raise TypeError(' size must be an integer')
    else:
        for _ in range(size):
            print("#" * size)
