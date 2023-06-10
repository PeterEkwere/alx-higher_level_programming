#!/usr/bin/python3

def print_list_integer(my_list=[]):
    i = 0
    length = len(my_list)
    for i in range(0, length):
        print("{:d}".format(my_list[i]))
