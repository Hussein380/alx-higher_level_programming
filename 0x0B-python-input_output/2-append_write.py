#!/usr/bin/python3
"""defines a write fucntion. that write text to a file"""


def append_write(filename="", text=""):
    """
    Appends the given text t the end of a file with the sepecified filename
    if the file doesnt exist it creates

    Args:
        filename  (str): the name of file to write to
        text (str): The  text to write the file

    Returns:
        int: The number of characters written to the file
    """

    """open the file in wite mode with URF_8 encoding"""

    count = 0
    with open(filename, 'a', encoding='utf-8', ) as file:
        return file.write(text)
