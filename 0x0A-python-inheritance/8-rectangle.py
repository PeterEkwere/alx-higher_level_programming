#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    This is a class module
    Author: Peter Ekwere

"""
if __name__ == "__main__":
    # Do not run directly
    print()


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This is a Rectangle class """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """ This is a public instance method area """
        raise Exception("area{} is not implemented")
