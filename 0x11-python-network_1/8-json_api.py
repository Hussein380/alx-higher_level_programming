#!usr/bin/python3

import requests
import sys

"""
Script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""

if __name__ == "__main__":
    # Check if any command-line argument is provided
    if len(sys.argv) == 1:
        # set q= "", if no argument is given
        q = ""

    else:
        # if an argument is given set q asa the first  argument
        q = sys.argv[1]
    try:
        # send a POST request to the specified URL with 'q' as the parameter
        response = requests.post('http://0.0.0.0:5000/search_user',
                                 data={'q': q})

        # Get the JSON response from the server
        json_response = response.json()

        # Check if the json response is not empty
        if json_response:
            # Display the id and name from the JSON response
            print("[{}] {}".format(json_response.get('id'),
                                   json_response.get('name')))

        else:
            # If json response is empty, print No result
            print("No result")

    except ValueError:
        # if the json response is invalid, print not a valid JSON
        print("Not a valid JSON")
