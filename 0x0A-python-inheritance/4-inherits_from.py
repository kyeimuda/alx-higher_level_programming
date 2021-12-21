#!/usr/bin/python3
# 4-inherits_from.py
"""
Module defines an inherited class-checking function.
"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance of a class\
     that inherited (directly or indirectly) from the specified class ; otherwise False
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
