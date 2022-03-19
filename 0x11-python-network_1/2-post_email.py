#!/usr/bin/python3
""" 
script that takes in a URL and an email, sends a POST request
"""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(resp.decode('utf-8'))
