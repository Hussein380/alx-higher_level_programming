import urllib.request
import sys

# Extract URL and email from command line arguments
url = sys.argv[1]
email = sys.argv[2]

# Encode email as bytes
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

# Send POST request to the URL with email as parameter
with urllib.request.urlopen(url, data=data) as response:
    # Decode and display the body of the response
    print(response.read().decode('utf-8'))
