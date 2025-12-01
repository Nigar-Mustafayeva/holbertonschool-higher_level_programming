#!/usr/bin/python3
"""
Fetches a URL and handles HTTP errors using requests
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        # Raise HTTPError for status codes >= 400
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(response.status_code))
