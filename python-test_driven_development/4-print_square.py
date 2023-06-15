#!/usr/bin/python3
"""create a function"""

def print_square(size):
    
     """Print the square using '#' character."""
     if not isinstance(size, int):
         """isinstance of size and int
         
         Raise TypeError if size must be an integer
         """
         raise TypeError('size must be an integer')
     elif not isinstance(size, int) or size < 0:
         """isinstance of size and int or size is negative
         
         
         Raise ValueError size must be menor than zero
         """
         raise ValueError('size must be >= 0')
     elif not isinstance(size, float) and size < 0:
         """isinstance of size and float or size is negative
         
         
         Raise TypeError size must be an integer
         """
         raise TypeError(' size must be an integer')
     else:
        for _ in range(size):
            """print size and # * size"""
            print("#" * size)
