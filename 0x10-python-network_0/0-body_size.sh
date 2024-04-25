#!/bin/bash
# Get the URL is provided as argument
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
