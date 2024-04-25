#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using binary tree search

    Args:
        list_of_integers: A list of unsorted integers

    Returns:
        A peak element  from the list, or None if the list is empty
    """

    # check if the list is empty
    if not list_of_integers:
        return None

    # Define the boundaries for binary search
    left, right = 0, len(list_of_integers) - 1

    # Binary search
    while left < right:
        mid = (left + right) // 2

        # Check if mid is a peak
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # peak found in the left half
            right = mid
        else:
            left = mid + 1
    # At the end of the loop, left and right will coverage  to a peak
    return list_of_integers[left]
