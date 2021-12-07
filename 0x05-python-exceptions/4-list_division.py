#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    ans = 0
    for index in range(list_length):
        try:
            ans = my_list_1[index] / my_list_2[index]
        except ZeroDivisionError:
            ans = 0
            print('division by 0')
        except TypeError:
            ans = 0
            print('wrong type')
        except IndexError:
            ans = 0
            print('out of range')
        finally:
            new_list.append(total)
    return new_list
