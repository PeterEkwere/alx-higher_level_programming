#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    This is a class module
    Author: Peter Ekwere

"""
if __name__ == "__main__":
    # Do not run directly
    print("Running directly")


class MyList(list):
    """ This is a subclass of list class """

    a_list = []

    def __init__(self):
        super().__init__()

    def append(self, digit):
        """ This is a Derived class method to override append """
        MyList.a_list.append(digit)

    def __str__(self):
        """ this would trigger when print or str is used """
        return "{}".format(MyList.a_list)

    def print_sorted(self):
        """ This is a class method that prints a sorted list """
        new_list = MyList.a_list[:]
        new_list = sorted(new_list, reverse=False)
        print(f"{new_list}")
