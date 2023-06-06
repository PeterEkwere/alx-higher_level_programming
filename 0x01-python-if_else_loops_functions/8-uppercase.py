#!/usr/bin/python3

def uppercase(str):
    i = 0
    upper = ""
    up = ""
    while i < len(str):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            up = chr(ord(str[i]) - 32)
            upper += up
            i += 1
        else:
            upper += str[i]
            i += 1
    print("{}".format(upper))
