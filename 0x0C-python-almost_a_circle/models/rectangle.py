#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import sys
from models.base import Base
sys.path.append("..")
"""
    This is a class module
    Author: Peter Ekwere

"""
if __name__ == "__main__":
    """ Do Not run Dirctly """


class Rectangle(Base):
    """
    This is a child class that would inherit from The base class
    """
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("x must be an integer")
        if y < 0:
            raise ValueError("x must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ This is the height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ This is the height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ This is x getter func """
        return self.__x

    @x.setter
    def x(self, value):
        """ This is x setter func """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ This is y getter func """
        return self.__y

    @y.setter
    def y(self, value):
        """ This is y setter func """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ This would return the Area of the rectangle """
        return self.height * self.width

    def display(self):
        """ this would Display the instance of the Rectangle """
        for row in range(self.__height):
            for items in range(self.__width):
                print("#", end="")
            print("")
