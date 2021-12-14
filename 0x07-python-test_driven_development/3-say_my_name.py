#!/usr/bin/python3
"""
function that prints full name
"""


def say_my_name(first_name, last_name=""):
    """
    fuction that prints a string in a formated manner
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
