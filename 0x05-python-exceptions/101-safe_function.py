#!/usr/bin/python3
# -*- coding :utf-8 -*-
import sys
"""
    This is a module
"""


def safe_function(fct, *args):
    result = 0
    try:
        result = fct(args[0], args[1])
        return result
    except Exception as e:
        sys.stderr.write("Exception: " + str(e) + "\n")
        return None
