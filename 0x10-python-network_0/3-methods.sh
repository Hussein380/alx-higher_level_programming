#!/bin/bash
#  takes in a URL and displays all HTTP methods the server will accept
curl -sI ALLOW $1 | grep "ALLOW" | cut -d " " -f2-
