#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    length = len(my_list)
    for index in new_list:
        for i in range(0, length):
            if new_list[i] == search:
                new_list[i] = replace
            else:
                new_list[i] = new_list[i]
        return new_list
