#!/usr/bin/python3
"""
Finds a peak in a list of
unsorted integers.
"""


def find_peak(list_of_integers):
    """
    finds the peak in the list
    Args: list_of_integers
    """
    if len(list_of_integers) == 0:
        return None

    l_int = list_of_integers
    size = len(l_int)
    
    if size == 1:
        return l_int[0]
    if size == 2:
        return max(l_int)
    
    mid = size//2
    mark = l_int[mid]
    if mark > l_int[mid - 1] and mark > l_int[mid + 1]:
        return mark
    elif mark < l_int[mid - 1]:
        return find_peak(l_int[:mid])
    else:
        return find_peak(l_int[mid + 1:])
