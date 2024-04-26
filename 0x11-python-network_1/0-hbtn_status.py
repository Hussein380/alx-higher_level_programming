#!/usr/bin/python3
import urllib.request

# URL of the website to fetch
url = 'https://alx-intranet.hbtn.io/status'

# Create a request object with the URL
req = urllib.request.Request(url)

# open the url as response and read it
with urllib.request.urlopen(req) as response:
    body = response.read()

# print the response body along with its type and decode content
print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
print("\t- utf8 content:", body.decode('utf-8'))
