#!/usr/bin/python3
""" a script takes in a URL and an email, sends a POST request """
import requests
import sys

if __name__ == "__main__":

    email = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], email)
    print(r.text)
