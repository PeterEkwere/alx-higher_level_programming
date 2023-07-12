#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    This is a Function Module
    author: peter ekwere

"""
if __name__ == "__main__":
    """ Do not run this directly """
    print()


def write_file(filename="", text=""):
    """
    This is a function that writes to and return from a file
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        Tfile = a_file.write(text)
    return Tfile
