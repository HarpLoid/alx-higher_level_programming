#!/usr/bin/python3
"""
Module - 5-text_indentation
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after
    each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in '.:?':
        text = text.replace(char, char + "\n\n")
    list_section = [section.strip(' ') for section in text.split('\n')]
    revised = "\n".join(list_section)
    print(revised, end="")
