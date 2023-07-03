#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    This is a Class module
    Author: peter ekwere

"""


class Rectangle:
    """
    This is a Rectangle class
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def __str__(self):
        if 0 in [self.__width, self.__height]:
            return ""
        else:
            matrix = ""
            for i in range(self.__height):
                row = []
                for i in range(self.__width):
                    matrix += "#"
                matrix += "\n"
            return matrix
