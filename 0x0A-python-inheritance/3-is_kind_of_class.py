#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    This is a module
    author: Peter Ekwere

"""
if __name__ == "__main__":
    # This should not be run directly
    print()


def is_kind_of_class(obj, a_class):
    """
    This is a class that checks is an object is an instance of a class
    """
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
