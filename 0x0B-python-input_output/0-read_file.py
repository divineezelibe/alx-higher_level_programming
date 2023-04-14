#!/usr/bin/python3
"""I created a module to read a text file"""


def read_file(filename="")
    """A method to read and print file content to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
