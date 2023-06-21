#!/usr/bin/python3
"""Define the class"""


class MyList(list):
    """print list sorted"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
