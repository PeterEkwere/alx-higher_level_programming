#!/usr/bin/python3
if __name__ == "__main__":
    # this is a script
    print("must be imported")


def print_list_integer(my_list=[]):
    i = 0
    length = len(my_list)
    for i in range(0, length):
        print("{}".format(my_list[i]))
