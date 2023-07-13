#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
    This is a class module
    Author: Peter Ekwere

"""
if __name__ == "__main__":
    """ Do not run Directly """


class Base:
    """
    This is a base class that would serve as a super class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
