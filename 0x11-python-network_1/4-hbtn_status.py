#!/usr/bin/python3
import requests

# URL to fetch
url = 'https://alx-intranet.hbtn.io/status'

# Sending a GET request to the URL and storing the response
response = requests.get(url)

# print the body response in specified format
print("Body reponse:")

# printing the type of response body
print("\t- type:", type(response.text))

# print the content of the repsonse
print("\t- content:", response.text)
