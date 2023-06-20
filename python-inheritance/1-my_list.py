#!/usr/bin/python3
"""Define the class"""


class MyList(list):
    """_summary_

    Args:
        list (_type_): append list a new list
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
