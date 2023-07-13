#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
    This is a class module
    Author: Peter Ekwere

"""
if __name__ == "__main__":
    """ Do not run Directly """

import sys
sys.path.append("..")
from models.base import Base

class Rectangle(Base):
    """
    This is a child class that would inherit from The base class
    """
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ This is the width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ This is the width setter """
        self.__width = value

    @property
    def height(self):
        """ This is the height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ This is the height setter """
        self.__height = value

    @property
    def x(self):
        """ This is x getter func """
        return self.__x

    @x.setter
    def x(self, value):
        """ This is x setter func """
        self.__x = value

    @property
    def y(self):
        """ This is y getter func """
        return self.__y

    @y.setter
    def y(self, value):
        """ This is y setter func """
        self.__y = value
