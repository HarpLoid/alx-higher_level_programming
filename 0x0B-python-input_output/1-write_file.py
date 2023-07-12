#!/usr/bin/python3
"""
Module - 1-write_file
"""


def write_file(filename="", txt=""):
    """ writes a string to a text file (UTF8)
        and returns the number of characters written """
    with open(filename, mode='w', encoding="utf-8") as f:
        return f.write(txt)
