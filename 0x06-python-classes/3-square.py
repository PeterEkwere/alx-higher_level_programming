#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" 
    This is a square class
    Author: Ekwere peter

"""

""" This is a Module """

if __name__ == "__main__":
    """ This will execue if run directly """
    print()


class Square:
    """ This is an Empty class """
    def __init__(self, size=0):
        """ check if the size is an integer """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """ This is a public instance method that returns the area of a Square """
    def area(self):
        return self.__size * self.__size
