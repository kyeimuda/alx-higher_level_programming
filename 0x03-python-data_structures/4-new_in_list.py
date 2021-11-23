#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0:
        return my_list
    elif idx >= length:
        return my_list
    elif idx >= 0 and idx < length:
        new = my_list[:]
        change = new[idx] = element
        return new
