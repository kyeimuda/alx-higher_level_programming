#!/bin/bash
#A script displays the size of the body of the response.
curl curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
