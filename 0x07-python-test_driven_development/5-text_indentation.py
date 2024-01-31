#!/usr/bin/python3
"""
This module introduces function def_indentation
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'

    Args:
        text: a string

    Raises:
        TypeError: if te inputs is not string

    Example:
    >>> text_indentation("Hello. How are you? I'm fine, thank you.")
    Hello
    How are you
    I'm fine thank you

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']
    new_line = True

    for char in text:
        if new_line and char == '':
            continue

        print(char, end='')

        if char in punctuations:
            print('\n')
            new_line = True

        else:
            new_line = False

    print('\n')
