#!/usr/bin/python3

import requests
import sys


def display_response(url):
    """
    displays url response
    Arguments:
        url - url given
    """
    # Send a GET requests to the provided url
    response = requests.get(url)
    # check if the status code of the response is greater than or equal to 400
    if response.status_code >= 400:
        # If so, print an error message with status code
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == "__main__":
    # Check if the correct number of argument are provided
    if len(sys.argv) != 2:
        #  if not, print Usage instructions and exit
        print("Usage: python 7-error_code.py <URL>")
        sys.exit(1)
    # Get the url from the cmd
    url = sys.argv[1]
    # call the display_response function with provided URl
    display_response(url)
