#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    This is a module
"""


def calculate_result(a, b):
    result = 0
    for i in range(1, 3):
        try:
            result += a ** b / i
        except Exception as e:
            if str(e) != 'Too far':
                raise
    return result + b + a
