#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order = sorted(a_dictionary)
    for index in order:
        print('{}: {}'.format(index, a_dictionary[index]))
