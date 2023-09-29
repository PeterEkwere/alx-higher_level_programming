#!/usr/bin/python3
"""
    This script sends a POST to the server
    Author: Peter Ekwere

"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    mail = sys.argv[2]
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    values = {'email': mail}
    headers = {'User-Agent': user_agent}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    request = urllib.request.Request(url, data, headers)
    with urllib.request.urlopen(request) as response:
        page = response.read()
        print(page.decode())
