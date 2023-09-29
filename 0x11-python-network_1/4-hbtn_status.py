#!/usr/bin/python3
"""
    This scripts sends request using the request package
    Author: Peter Ekwere
"""
import requests


if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))