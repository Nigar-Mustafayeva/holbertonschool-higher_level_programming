#!/usr/bin/python3
"""
This is documentation for module
"""


import urllib.request 
req = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    the_page = response.read()
