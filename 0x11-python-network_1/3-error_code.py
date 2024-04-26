#!/usr/bin/python3
import urllib.error
import urllib.request
import sys

if __name__ == "__main__":
    # Extracting the URL from the command line arguments
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            # Reading the response body and decoding it as UTF-8
            body = response.read().decode('utf-8')
            # Printing the decode response
            print(body)
    except urllib.error.HTTPError as e:
        # Handling HTTP errors and printing the error code
        print("Error code:", e.code)
