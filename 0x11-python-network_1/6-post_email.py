#!/usr/bin/python3

import requests
import sys
# Extracting URL and email from command line argument
url = sys.argv[1]
email = sys.argv[2]

# Sending POST request with email as parameter
response = requests.post(url, data={'email': email})

# Displaying the body of the response
print(response.text)
