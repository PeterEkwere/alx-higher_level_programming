#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    key_to_delete = []
    for key, v in a_dictionary.items():
        if v == value:
            key_to_delete.append(key)

    for keys in key_to_delete:
        del(a_dictionary[keys])
    return a_dictionary
