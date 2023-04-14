#!/usr/bin/python3
"""
Another Module with class Student
"""


class Student:
    """
        A class students that defines a student by attributes, etc.
    """
    def __init__(self, first_name, last_name, age):
        """
            Initialize Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
            Fetch a dictionary representation of Student.
        """

        if attr is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__
