#!/usr/bin/python3

def search_replace(my_list, search, replace):
    for i in my_list:
        if search == i:
            idx = my_list.index(search)
            my_list[idx] = replace

    return (my_list)
