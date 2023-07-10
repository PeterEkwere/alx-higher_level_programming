#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    This is a class module
    Author: Peter Ekwere

"""
if __name__ == "__main__":
    # Do not run directly
    print()


class BaseGeometry:
    """ This is a BaseGeometry class """
    def __init__(self):
        pass

    def area(self):
        """ This is a public instance method """
        raise Exception("area{} is not implemented")
