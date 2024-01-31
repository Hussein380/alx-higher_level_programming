#!/usr/bin/python3
"""" shebang / script a code"""

def print_last_digit(number):
    """function that prints the last digit of a number."""

    #if number is less than zero , to get las digit , divide by zero
    if number < 0:
        last_digit = number % -(10)
        print(-(last_digit), end='')
    else:

        last_digit = number % 10
        print(last_digit, end='')
    #return absoulute value
    return abs(last_digit)
