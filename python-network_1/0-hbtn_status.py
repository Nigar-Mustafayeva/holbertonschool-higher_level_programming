#!/usr/bin/python3
"""
This is documentation for module
"""


import urllib.request

url = "https://intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    the_page = response.read()
    page_as_a_string = the_page.decode('utf-8')
    print(page_as_a_string)
