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
        """
        Initialize a new rectangle

        width: this is an integer
        height: this is an integer
        """
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """ getter for the attr height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for the attr height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ getter for the attr width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for the attr width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
