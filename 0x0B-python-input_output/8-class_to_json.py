#!/usr/bin/pythhon3
#8-class_to_json.py
"""
This module defines a function that returns\
 a json representation of an object
"""


def class_to_json(obj):
    """
    function that returns a json representation of\
    the obj object
    """
    return obj.__dict__
