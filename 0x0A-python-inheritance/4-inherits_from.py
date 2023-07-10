#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    This is a module
    author: Peter Ekwere

"""
if __name__ == "__main__":
    # This should not be run directly
    print()


def inherits_from(obj, a_class):
    """
    This is a function that checks if obj
    is an instance of a class thath inherited(directly or indirectly)
    fromm the class "a_class"
    """
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
