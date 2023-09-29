#!/usr/bin/python3
"""
    This scripts GETS a header variable
    Author: Peter Ekwere

"""
import sys
import urllib.request


url = sys.argv[1]

response = urllib.request.urlopen(url)

value = response.headers.get('X-Request-Id')

print(value)
