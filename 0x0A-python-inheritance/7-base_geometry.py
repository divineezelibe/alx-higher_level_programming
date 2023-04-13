#!/usr/bin/python3
"""A new module with class BaseGeometry"""


def area(self):
    
    """Calculate area"""
    raise Exception("area() is not implemented")

def integer_validator(self, name, value):
    """Validate if number is integer"""
    
    if type(value) is not int:
        raise TypeError("{} must be an integer".format(name))
    if value <= 0:
        raise ValueError("{} must be greater than 0".format(name))
