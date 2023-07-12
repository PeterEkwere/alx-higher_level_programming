#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    This is a Function Module
    author: peter ekwere

"""
if __name__ == "__main__":
    """ Do not run this directly """


def class_to_json(obj):
    """
    This is a function that returns dictionary
    repr of all attributes of obj
    """
    return obj.__dict__
