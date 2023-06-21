#!/usr/bin/python3
"""validate the object and class"""


def is_same_class(obj, a_class):
    if isinstance(obj , a_class):
        return False
    else:
        return True
