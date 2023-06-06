#!/usr/bin/python3
def print_last_digit(number):
    str_num = str(number)
    last = int(str_num[-1:])
    print("{}".format(last))
    return last
