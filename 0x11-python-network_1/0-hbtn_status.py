#!/usr/bin/python3
"""
    This module implements the urllib package
    Author: Peter Ekwere

"""
import urllib.request

if __name__ == "__main__":
    res = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(res) as a:
        html = a.read()
        html_string = html.decode()
        print("Body response:")
        print("\t- type: <class '{}'".format(type(html).__name__))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html_string))
