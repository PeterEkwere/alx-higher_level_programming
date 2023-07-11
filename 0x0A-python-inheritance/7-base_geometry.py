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
        """
        This is a public instance method area
        """
        raise Exception("area{} is not implemented")

    def integer_validator(self, name, value):
        """
        This is an instance method that validates a value
        """
        if isinstance(value, str):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
