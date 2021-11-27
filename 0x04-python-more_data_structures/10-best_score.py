#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None or len(a_dictionary) < 1:
        return None
    else:
        maxi = max(a_dictionary)
        return maxi
