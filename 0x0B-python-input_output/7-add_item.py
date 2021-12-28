#!/usr/bin/python3
import json
"""
This module adds all arguments to a Python list, and\
 then save them to a file
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation
    """
    with open(filename, "w") as f:
        return (json.dump(my_obj, f))
