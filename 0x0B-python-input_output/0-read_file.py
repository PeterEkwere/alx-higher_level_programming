#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    This is a module
    author: peter ekwere

"""
if __name__ == "__main__":
    """ Do nut Run Directly """
    print()


def read_file(filename=""):
    """
    This function reads a text file UTF8 and prints
    """
    with open(filename, encoding="utf-8") as a_file:
        print("{}".format(a_file.read().rstrip()))
