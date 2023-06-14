#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    number = 0
    roman_constants = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                       'C': 100, 'D': 500, 'M': 1000}

    for i, j in zip(roman_string, roman_string[1:]):
        if i not in roman_constants.keys():
            return 0
        elif roman_constants[i] >= roman_constants[j]:
            number += roman_constants[i]
        else:
            number -= roman_constants[i]
    number += roman_constants[roman_string[-1]]

    return number
