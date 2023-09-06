#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if ord(char) => 97 and ord(char) <= 122:
            print("{:c}".format(ord(char) - 32), end="")
        else:
            print("{:c}".format(ord(char)), end="")
    print()
