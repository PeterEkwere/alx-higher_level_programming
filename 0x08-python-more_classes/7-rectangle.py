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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle

        width: this is an integer
        height: this is an integer
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol = []

    def area(self):
        """ returns the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ returns the perimeter of the rectangle """
        return 2 * (self.__width + self.__height)

    @property
    def height(self):
        """ getter of the attr height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter of the attr height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ getter of the attr width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter of the attribute width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def __str__(self):
        """ __str__ is called when str or print is used """
        if 0 in [self.__width, self.__height]:
            return ""
        else:
            matrix = ""
            for i in range(self.__height):
                for i in range(self.__width):
                    matrix += " ".join(str(symbol) for symbol in Rectangle.print_symbol)
                matrix += "\n"
            return matrix

    def __repr__(self):
        """ __repr__ is called when repr is used """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ __del__ is called when del is used """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
