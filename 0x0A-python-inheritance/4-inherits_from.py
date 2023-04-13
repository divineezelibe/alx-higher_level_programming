#!/usr/bin/python3
"""Another module with a method called inherits_from"""


def inherits_from(obj, a_class):
    """This method returns True if object
    is an instance of the base class, else return false"""

    return isinstance(obj, a_class) and type(obj) != a_class
