#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    This is a Function Module
    author: peter ekwere

"""
if __name__ == "__main__":
    """ Do not run this directly """

import json
import sys
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_item():
    """
    This is a function that manipulates json file
    """
    filename = "add_item.json"
    my_list = load_from_json_file(filename) if os.path.isfile(filename) else []
    i = 1

    while i < len(sys.argv):
        my_list.append(sys.argv[i])
        i += 1

    save_to_json_file(my_list, filename)


add_item()
