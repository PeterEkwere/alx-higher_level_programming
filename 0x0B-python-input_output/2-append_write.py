#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
    This is a function module
    Author: peter ekwere

"""
if __name__ == "__main__":
    """ Do Not run Directly """
    print()


def append_write(filename="", text=""):
    """
    This is a function that appends to a file and returns the amount
    """
    with open(filename, mode='a', encoding="utf-8") as a_file:
        num = a_file.write(text)
    return num
