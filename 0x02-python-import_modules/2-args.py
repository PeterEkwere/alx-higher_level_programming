#!/usr/bin/python3

if __name__ == "__main__":
    import sys

i = 0
j = 1

while i < len(sys.argv) - 1:
    i += 1


if len(sys.argv) == 1:
    print(f"0 arguments.")
elif len(sys.argv) == 2:
    print(f"{1} argument:")
    print(f"{1}: {sys.argv[j]}")
else:
    print(f"{i} arguments:")
    while j < len(sys.argv):
        print(f"{j}: {sys.argv[j]}")
        j += 1
