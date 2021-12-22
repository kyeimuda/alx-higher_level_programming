#!/usr/bin/python3
# 8-load_from_json_file.py
"""
This module defines a JSON file-reading function.
"""
import json


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”:
    """
    with open(filename) as f:
        return json.load(f)
