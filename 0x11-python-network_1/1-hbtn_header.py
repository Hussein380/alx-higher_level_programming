#!/usr/bin/python3
"""
This script takes URL as input, sends a request to the URL,
and displays the value of the X-Request-Id variable found in the header
"""

import urllib.request
import sys

# Check if the correct number of argument is provided
if len(sys.argv) != 2:
    print("Usage: ./1-hbtn_header.py <URL>")
    sys.exit(1)

url = sys.argv[1]

# send a reqest to the URL
try:
    with urllib.request.urlopen(url) as response:
        # check if X-Request_Id exists in the response headers
        if 'X-Request-Id' in response.headers:
            request_id = response.headers['X:-Request-Id']
            print(request_id)
        else:
            print("X-Request-Id not found in the response headers.")
except Exception as e:
    print("Error:", e)
