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


def load_from_json_file(filename):
    """
    This Function deserializes an object from json file
    """
    with open(filename, mode='r', encoding="utf-8") as a_file:
        json_string = a_file.read()
        file_object = json.loads(json_string)

    return file_object
