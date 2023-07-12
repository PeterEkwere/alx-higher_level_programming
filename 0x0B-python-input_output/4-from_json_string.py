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


def from_json_string(my_obj):
    """
    This Function serializes an object
    """
    json_string = json.loads(my_obj)
    return json_string
