#!/usr/bin/python3
"""
Fetches the X-Request-Id header from a URL using requests
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
