#!/usr/bin/python3
"""
Sends a letter to the search_user API and handles JSON response
"""

import requests
import sys

if __name__ == "__main__":
    # Get the letter from command line or default to empty string
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}

    try:
        response = requests.post(url, data=data)
        # Attempt to parse JSON
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")
    except ValueError:
        # JSON decoding failed
        print("Not a valid JSON")
