#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

#print(add_integer(1, 2))
print(add_integer(-10, -10))
print(add_integer(0.5, 0.5))
print(add_integer(2**31, 2**31))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
