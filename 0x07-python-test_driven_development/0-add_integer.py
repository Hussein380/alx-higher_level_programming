#!/usr/bin/python3
"""
This module contain the add fucntion only
"""
def add_integer(a, b=98):
    """
    Adds two integers : a and b

    Args:
        a(int or float): The first operand
        b(int or float): The seconfd operand

    Returns:
         int, the sum of a and b

    Raises:
        TypeError: if a or b is not an integer or float

    """

    #check if a is not an int or float
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    #check if b is not  an int or float
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    """
    if not isinstance(a ,( int,float)) and  if not isinstance(b ,(int,float)):
        raise TypeError("a must be an integer")
    """
    #cast a and b intagers if they are float

    a  = int (a)
    b = int(b)
    #return the sum
    return a + b
