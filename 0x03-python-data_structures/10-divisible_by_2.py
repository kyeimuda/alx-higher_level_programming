#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list = []
    for index in my_list:
        if index % 2 == 0:
            index = True
            list.append(index)
        else:
            index = False
            list.append(index)
    return list
