#!/bin/bash
# takes in a URL as an argument, sends a GET request to the URL, displays the body of the response
curl -sX GET $1 -H "X-School-USER-Id: 98" -L
