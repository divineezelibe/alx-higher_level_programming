#!/usr/bin/python3
"""I created a module that appends sting at the file end"""


def append_write(filename="", text=""):
    """A method that appends the string"""
    with open(filename, mode="a+", encoding="utf-8") as f:
        return f.write(text)
