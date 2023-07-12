#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    This is a module
    author:peter ekwere

"""
if __name__ == "__main__":
    """ DO not run directly """
    print()

import json


def save_to_json_file(my_obj, filename):
    """
    This Function serializes an object and adds it to a file
    """
    json_string = json.dumps(my_obj)

    with open(filename, mode='w', encoding="utf-8") as a_file:
        a_file.write(json_string)
