#!/usr/bin/python3
"""" Defines a function tha reads a text file """


def read_file(filename=""):
    """
    Introduces a functions that read a file and prints it to the stdout

    Args:
        filename: the name of the file to read text from

    Return:
        None
    """

    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
