#!/usr/bin/python3
"""
    This is a module
    Author: Peter Ekwere

"""


def say_my_name(first_name, last_name=""):
    """
    This is a function that prints a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
