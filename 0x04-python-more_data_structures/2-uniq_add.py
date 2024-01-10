#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set()
    sum_unique = 0

    for element in my_list:
        if element not in unique_set:
            unique_set.add(element)
            sum_unique += element
    return sum_unique
