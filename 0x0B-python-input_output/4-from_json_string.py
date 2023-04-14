#!/usr/bin/python3
"""
A module to convert string object to JSON
"""
import json


def from_json_string(my_str):
    """
    A method to return string object
    """
    return json.loads(my_str)
