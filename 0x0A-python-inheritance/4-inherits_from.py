#!/usr/bin/python3
"""4-inherits_from"""


def inherits_from(obj, a_class):
    """
    this function returns True if the object is an instance of a class
    inherited directly or indirectly
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
