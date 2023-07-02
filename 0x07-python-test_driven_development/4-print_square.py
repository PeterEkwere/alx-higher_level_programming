#!/usr/bin/python3
# -*- coding utf-8 -*-
"""
    This is a module
    Author: Peter Ekwere

"""


def print_square(size):
    i = 0
    j = 0

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    if isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    while i < size:
        j = 0
        while j < size:
            print("#", end="")
            j += 1
        print("")
        i += 1
