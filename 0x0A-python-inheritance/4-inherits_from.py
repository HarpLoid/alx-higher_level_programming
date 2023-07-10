#!/usr/bin/python3
"""
Module - 4-inherits_from
Returns True if the object is an instance of a class that
inherited (directly or indirectly)
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of
    a class that inherited (directly or indirectly)
    from the specified class ; otherwise False.
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)