#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    sorted_dict = {i: a_dictionary[i] for i in keys}
    for k, v in sorted_dict.items():
        print("{} : {}".format(k, v))
