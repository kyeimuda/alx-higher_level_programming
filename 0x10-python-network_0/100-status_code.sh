#!/bin/bash
#A script displays only the status code of the response.
curl -s -o /dev/null -sIw "%{http_code}" "$1"
