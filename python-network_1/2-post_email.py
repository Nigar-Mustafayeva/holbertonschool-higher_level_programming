#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email as form data
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Create a Request object with the data (POST)
    req = urllib.request.Request(url, data=data)

    # Send the request and read the response
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
