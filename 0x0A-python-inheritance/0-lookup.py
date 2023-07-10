#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    This is a Module that returns the __dict__
    Author: Peter Ekwere

"""
if __name__ == "__main__":
    # This will execute if run directly
    print("hello")


def lookup(obj):
    """ The lookup function returns a list of attr and meth of an object """
    return list(dir(obj))
