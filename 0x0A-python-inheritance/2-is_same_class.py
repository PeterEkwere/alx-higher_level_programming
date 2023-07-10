#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    This is Module
    Author: Peter Ekwere

"""
if __name__ == "__main__":
    # This is triggerd if run directly
    print("")


def is_same_class(obj, a_class):
    """
    This is a function that returns true if obj is an instance of a_class
    """
    return type(obj) is a_class
