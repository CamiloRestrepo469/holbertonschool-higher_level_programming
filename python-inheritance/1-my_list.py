#!/usr/bin/python3
"""Define the class"""

class MyList(list):
    """_summary_

    Args:
        list (_type_): _description_
    """
    def print_sorted(self):
        """_summary_
        """
        sorted_list = sorted(self)
        print(sorted_list)
