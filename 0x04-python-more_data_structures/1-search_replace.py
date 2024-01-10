#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:1] + [replace] + my_list[2:]

    return new_list
