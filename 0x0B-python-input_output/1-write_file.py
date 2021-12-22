#!/usr/bin/python3
# 3-write_file.py
"""
This module defines a file-writing function.
"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8) and\
        returns the number of characters written
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        characters = f.write(text)
        return (characters)
