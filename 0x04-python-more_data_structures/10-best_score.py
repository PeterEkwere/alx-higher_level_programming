#!/usr/bin/python3

def best_score(a_dictionary):
    name = ""
    score = 0

    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    for k, v in a_dictionary.items():
        if v > score:
            score = v
            name = k
    return name
