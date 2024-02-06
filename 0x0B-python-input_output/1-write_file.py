#!/usr/bin/python3
"""defines a write fucntion. that write text to a file"""


def write_file(filename="", text=""):
    """
    Write a text to a file and return the number of characters written

    Args:
        filename  (str): the name of file to write to
        text (str): The  text to write the file

    Returns:
        int: The number of characters written to the file
    """

    """open the file in wite mode with URF_8 encoding"""
    with open(filename, 'w', encoding='utf-8', ) as file:

        """write text to the file"""
        file.write(text)

        return len(text)
