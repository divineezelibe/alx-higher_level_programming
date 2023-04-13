#!/usr/bin/python3
"""Another module with a method called is_kind_of_class"""

def is_kind_of_class(obj, a_class):
    """Returns True if object is an instance of a class it inherits froms"""

    return isinstance(obj, a_class)
