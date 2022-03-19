#!/usr/bin/python3
"""
A scripr displays the value of the X-Request-Id variable
"""
import requests
import sys

if __name__ == "__main__":
    argument = sys.argv[1]
    r = requests.get(argument)
    print(r.headers.get('X-Request-Id'))
