#!/usr/bin/python3
"""I created a module that write to a file"""

def write_file(filename="", text=""):
    """A method that writes a string to file and returns the
    length"""
    with open(filename. encoding="utf-8", mode="w+") as f:
        return f.write(text)
