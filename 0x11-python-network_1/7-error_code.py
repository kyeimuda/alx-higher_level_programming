#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL and
displays the body of the response with Requests library.
"""
import requests
import sys

if __name__ == "__main__":

    error = requests.get(sys.argv[1])
    if error.status_code >= 400:
        print('Error code: {}'.format(error.status_code))
    else:
        print(error.text)
