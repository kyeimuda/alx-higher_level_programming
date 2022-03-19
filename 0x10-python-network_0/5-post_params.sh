#!/bin/bash
# A bash script that sends a POST request to the passed URL, and
curl -sX POST "$1" --data "email=test@gmail.com&subject=I will always be here for PLD"
