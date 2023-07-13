#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    This is a Class Module
    author: peter ekwere

"""
if __name__ == "__main__":
    """ Do not run this directly """


class Student:
    """
    This is a Student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        my_dict = {}
        if isinstance(attrs, list):
            for attr in attrs:
                if attr not in self.__dict__:
                    pass
                else:
                    my_dict.update({attr: getattr(self, attr)})
            return my_dict
        return self.__dict__

    
