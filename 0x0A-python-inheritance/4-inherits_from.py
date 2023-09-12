#!/usr/bin/python3
"""
A method for checking if a class is inheriteed
"""


def inherits_from(obj, a_class):
    """
    It returns true if an object is inherited
    """
    return (issubclass(type(obj), a_class) and type != a_class)
