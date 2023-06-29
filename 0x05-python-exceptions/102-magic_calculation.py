#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    This is a module
"""


def calculate_result(a, b):
    result = 0

    for i in range(1, 4):
        try:
            if i < a:
                raise Exception("Too far")
            result += (a ** b) / i
        except:
            result += a + b

    return result
