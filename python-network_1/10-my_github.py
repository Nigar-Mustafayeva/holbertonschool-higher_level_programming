#!/usr/bin/python3
"""
Fetches your GitHub user ID using the GitHub API with Basic Authentication
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, token))
        json_data = response.json()
        print(json_data.get('id'))
    except requests.exceptions.RequestException:
        print(None)
