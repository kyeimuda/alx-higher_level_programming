#!/usr/bin/python03
def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0:
        return my_list
    elif idx >= length:
        return my_list
    elif idx >= 0 and idx < length:
        change = my_list[idx] = element
        return my_list
