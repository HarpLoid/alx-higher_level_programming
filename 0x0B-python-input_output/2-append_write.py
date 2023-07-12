#!/usr/bin/python3
"""
Module - 2-append_write
"""


def append_write(filename="", txt=""):
    """ appends a string at the end of a text file (UTF8)
        and returns the number of characters written """
    with open(filename, mode='a', encoding="utf-8") as f:
        return f.write(txt)
