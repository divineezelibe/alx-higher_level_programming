#!/usr/bin/python3
"""Rectangle that defines a rectangle with private instance variables"""

class Rectangle:
    """Rectangle class build up"""

    def __init__(self, width = 0, height = 0):
        """Start a rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter for the width o the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """etter for height"""
        return self.__height

    @height.setter
    def height (self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
