#!/usr/bin/python3
"""Define the kind of class"""


def inherits_from(obj, a_class):
    """return a instance of a class"""
    if not type(obj) is a_class:
        return True
    else:
        return False
