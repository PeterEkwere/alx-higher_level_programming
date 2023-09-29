#!/usr/bin/python3
"""
    This scripts sends request using the request package
    Author: Peter Ekwere
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print("Error code: {}".format(response.status_code))
