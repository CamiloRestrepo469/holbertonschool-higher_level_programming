#!/usr/bin/python3
"""Define inheritance for classes"""


def inherits_from(obj, a_class):
    """define type inheritance"""
    return isinstance(obj, a_class) and type(obj) != a_class
