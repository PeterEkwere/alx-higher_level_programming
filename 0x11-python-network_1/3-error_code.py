#!/usr/bin/python3
"""
    This script basically handles request errors
    Author:Peter Ekwere
"""
import sys
import urllib.request
from urllib.error import HTTPError


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            body = response.read()
            print(body.decode())
    except HTTPError as e:
        print(f"Error code: {e.code}")
