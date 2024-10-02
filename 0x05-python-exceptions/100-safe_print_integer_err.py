#!/usr/bin/python3
# Function to safely print an integer and handle errors
def safe_print_integer_err(value):
    try:
        # Try to format the value as an integer and print it
        print("{:d}".format(value))
        # If successful, return True
        return True
    except (ValueError, TypeError) as e:
        # If an error occurs (not a valid integer), print an error message to stderr
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        # Return False because the value could not be printed as an integer
        return False

