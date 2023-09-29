#!/usr/bin/python3
"""
    This module implements the urllib package
    Author: Peter Ekwere

"""
import urllib.request


res = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(res) as a:
    html = a.read()
html_string = html.decode()
print(f"""Body response:
        - type: <class '{type(html).__name__}'>
        - content: {html}
        - utf8 content: {html_string}""")
