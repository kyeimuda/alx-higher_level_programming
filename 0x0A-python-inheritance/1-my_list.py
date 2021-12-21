#!/usr/bin/python3
# 1-my_list.py
"""
Defines an inherited list class MyList.
"""


class MyList(list):
    """
    a class MyList that inherits from list.
    """

    def print_sorted(self):
        """
        Prints a list in sorted ascending order.
        """
        print(sorted(self))
