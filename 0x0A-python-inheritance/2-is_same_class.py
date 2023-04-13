#!/usr/bin/python3
"""Another module with a method is_same_class"""


def is_same_class(obj, a_class):
    """This method returns True if an object is an instance of a class"""

    return type(obj) is a_class
