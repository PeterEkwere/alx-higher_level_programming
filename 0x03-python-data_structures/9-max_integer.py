#!/usr/bin/python3

def max_integer(my_list=[]):
    j = 0

    if len(my_list) == 0:
        return None

    for i in range(len(my_list)):
        if my_list[i] > j:
            j = my_list[i]
    return j
