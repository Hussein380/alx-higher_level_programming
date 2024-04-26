#!/usr/bin/python3
"""
"Python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header
"""

import requests
import sys

if __name__ == "__main__":
    # check if the number of argument is correct
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    # Send a Get request to the URL
    response = requests.get(url)

    # check if the request was successfull(status code 200)
    if response.status_code == 200:
        #  check if the X-Request-Id header is present in the response
        if 'X-Request-Id' in response.headers:
            # Display the value of the X-Requests_Id header
            print(response.headers['X-Request-Id'])
        else:
            print("No X-Request-Id header found in the response.")
            sys.exit(1)
    else:
        print("Error: {}".format(response.status_code))
        sys.exit(1)
