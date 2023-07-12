#!/usr/bin/python3
"""
Module - 0-read_file
"""


def read_file(filename=""):
    """ Reads content of a file """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
