#!/usr/bin/python3
"""A Module to return the JSON representation of
of an object(String)"""
import json


def to_json_string(my_obj):
    """
    A method to return it
    """
    return json.dumps(my_obj)
