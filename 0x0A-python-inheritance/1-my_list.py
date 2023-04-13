#!/usr/bin/python3
"""Create MyList module class"""


class MyList(list):
    """MyList that inherits from list"""
    
    def print_sorted(self):
        """Print sorted list already"""
        print(sorted(self))
