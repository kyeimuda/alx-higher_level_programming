#!/usr/bin/python3
# 4-append_write.py
"""
This module defines a file-appending function.
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file\
        (UTF8) and returns the number of characters added.
    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        characters = f.write(text)
        return (charaters)
