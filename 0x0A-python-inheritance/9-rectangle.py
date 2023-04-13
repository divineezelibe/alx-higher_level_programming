#!/usr/bin/python3
"""Module with a class Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Method initialized on instantiation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate or redefine he area method in the base class"""

        return self.__width * self.__height

    def __str__(self):
        """Return the next string"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
