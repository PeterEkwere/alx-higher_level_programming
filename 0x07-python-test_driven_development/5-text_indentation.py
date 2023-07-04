#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    This is a module
    Author: Peter Ekwere

"""


def text_indentation(text):
    """
    text_indetation is a function that prints every text excempting [?, :, .]

    Args:
        Text is a list of characters

    Return:
        nothing
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
    
