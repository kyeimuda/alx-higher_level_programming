#!/usr/bin/python3
def max_integer(my_list=[]):
    biggest = 0
    holder2 = my_list[:]
    length = len(my_list)
    if length == 0:
        return None
    elif length > 0:
        for index in my_list:
            holder = my_list[0]
            biggest = my_list[0]
            for i in range(1, length):
                if holder < holder2[i]:
                    holder = holder2[i]
                    biggest = holder2[i]
        return biggest
