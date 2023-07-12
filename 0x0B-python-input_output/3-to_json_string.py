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


def to_json_string(my_obj):
    """
    This Function serializes an object
    """
    json_string = json.dumps(my_obj)
    return json_string
