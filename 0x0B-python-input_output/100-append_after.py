#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
    This is a function module
    Author: peter ekwere

"""
if __name__ == "__main__":
    """ Do Not run Directly """
    print()


def append_after(filename="", search_string="", new_string=""):
    """
    This is a function that appends to a file and returns the amount
    """
    with open(filename, mode='r+', encoding="utf-8") as a_file:
        content = a_file.read()
        new_content = content.replace(search_string, search_string + new_string)
        a_file.seek(0)
        a_file.write(new_content)
        a_file.truncate
