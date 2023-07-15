#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import json
"""
    This is a class module
    Author: Peter Ekwere

"""
if __name__ == "__main__":
    """ Do not run Directly """


class Base:
    """
    This is a base class that would serve as a super class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This function will return a json string representation of list_dict
        """
        if list_dictionaries == None or list_dictionaries == []:
            return
        else:
            json_string = json.dumps(list_dictionaries)
            return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This will save a json string representation of list_objs to a file
        """
        json_list = []
        for object in list_objs:
            json_list.append(object.to_dictionary())

        json_string = json.dumps(json_list)
        
        filename = f"{cls.__name__}.json"
        with open(filename, mode='w', encoding="utf-8") as a_file:
            a_file.write(json_string)
