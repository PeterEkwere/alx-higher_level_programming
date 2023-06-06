#!/usr/bin/python3
for i in range(1, 100):
    if i < 99:
        print("{:2d}, ".format(i), end="")
    if i == 99:
        print("{}".format(i))
