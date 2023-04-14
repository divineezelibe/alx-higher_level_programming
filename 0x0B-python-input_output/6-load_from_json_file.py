#!/usr/bin/python3
"""A module  that creates an Object from JSON file"""
import json


def load_from_json_file(filename):
    """
    A method that loads and returns it
    """
    with open(filename, "r") as f:
        my_obj = json.load(f)
        return my_obj 
