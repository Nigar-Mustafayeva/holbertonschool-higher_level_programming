#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter using requests
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Create the payload dictionary
    data = {'email': email}

    # Send POST request
    response = requests.post(url, data=data)

    # Print the response body
    print(response.text)
