#!/usr/bin/python3

"""Appending to a file"""


def append_write(filename="", text=""):
    """
    append a string to the end of a text file
    returns the number of characters added
    """

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
