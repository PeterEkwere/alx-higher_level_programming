#!/usr/bin/python3
"""
    This is a class module
    author: peter Ekwere

"""


class LockedClass:
    """
    This is a locked class
    """
    def __setattr__(cls, name, value):
        raise AttributeError("'LockedClass' object has "
                             "no attribute 'last_name'")
