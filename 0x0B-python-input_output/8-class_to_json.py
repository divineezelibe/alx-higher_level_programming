#!/usr/bin/python3
"""
Module that returns the dictionary desc
"""


def class_to_json(obj):
    """
        Method that returns dictionary representation with simple data structure.
    """
    return obj.__dict__
