#!/usr/bin/python3

import urllib.request

"""
Display the body of the response.
- type: the type of the response content.
- content: the actual body of the response.
"""
url = 'https://alx-intranet.hbtn.io/status'

# Open the URL and retrieve the response
with urllib.request.urlopen(url) as response:
    # Read the response content and decode it as UTF-8
    body = response.read()
    utfContent =  body.decode("utf-8")
    
print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
print ("\t- utf8 content:", utfContent)
