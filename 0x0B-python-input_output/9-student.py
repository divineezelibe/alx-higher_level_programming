#!/usr/bin/python3
"""
A Module with a class Student.
"""


class Student:
    """
        A class named students that defines a student by attributes, etc.
    """
    def __init__(self, first_name, last_name, age):
        """
            Initialize Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            retrieves a dictionary representation of Student.
        """
        return self.__dict__
