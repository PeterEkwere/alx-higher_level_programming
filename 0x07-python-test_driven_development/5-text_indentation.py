#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    This is a module
    Author: Peter Ekwere

"""


def text_indentation(text):
    for word in text:
        print(f"{word}", end="")
        if word == '.' or word == '?' or word == ':':
            print("")
            print("")
        elif word == ' ':
            print(' ', end='')
        else:
             print('', end='')
