#!/usr/bin/python3
# -*- code: utf-8 -*-
import sys
"""
    This module prints only integers
"""


def safe_print_integer_err(value):
    Error = "Exception: Unknown format code 'd' for object of type 'str'\n"
    try:
        int_value = (value)
        print("{:d}".format(int_value))
        return True
    except ValueError:
        sys.stderr.write(Error)
        return False
