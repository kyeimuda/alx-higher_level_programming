#!/usr/bin/python3
"""A python script that displays the value of the X-Request-Id variable"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers['X-Request-Id'])
