#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            raise ValueError("Value not an intager")
    except ValueError:
        return False
