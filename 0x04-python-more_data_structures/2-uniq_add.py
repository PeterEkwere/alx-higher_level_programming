#!/usr/bin/python3

def uniq_add(my_list=[]):
    if len(my_list) == 0:
        return 0
    set1 = set(my_list)
    list1 = list(set1)
    num = 0

    for i in list1:
        num = num + i

    return num
