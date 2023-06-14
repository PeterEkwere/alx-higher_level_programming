#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    set3 = set()
    set3 = set_1 - set_2
    set4 = set_2 - set_1
    set5 = set3.union(set4)
    return set5
