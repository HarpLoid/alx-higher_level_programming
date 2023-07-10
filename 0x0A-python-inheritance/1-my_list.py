#!/usr/bin/python3
"""
Module - 1-my_list
Class that inherits from
list
"""


class MyList(list):
    """
    Inherits from list
    
    Methods:
        print_sorted(self)
    """
    def print_sorted(self):
        """
        prints the sorted list
        """
        print(sorted(self))