#!/usr/bin/python3

import sys

i = 0
while i < len(sys.argv) - 1:
    i += 1

if len(sys.argv) == 1:
    print(f"0 arguments.")
else:
    j = 1
    print(f"{i} argments:")
    while j < len(sys.argv):
        print(f"{j}: {sys.argv[j]}")
        j += 1
