#!/bin/bash
#  A bash script that sends a GET request to the URL, and displays
#the body of the response
curl -sH "X-School-User-Id" -X GET "$1"
