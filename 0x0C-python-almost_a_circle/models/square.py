#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import sys
from models.rectangle import Rectangle
sys.path.append("..")
"""
    This is a class module
    Author: Peter Ekwere

"""
if __name__ == "__main__":
    """ Do Not run Dirctly """


class Square(Rectangle):
    """
    This is a child class that would inherit from The base class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ This is the __init__ function """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ This function overrides the __str__ call """
        return f"[Square] ({self.id})" \
               f" {self.x}/{self.y} - {self.height}"
