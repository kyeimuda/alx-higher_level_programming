#!/usr/bin/python3
# 11-square.py
"""
This module defines a Rectangle subclass Square.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class for a square.
    """

    def __init__(self, size):
        """
        Instantiation of a  square class.
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
