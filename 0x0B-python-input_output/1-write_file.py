#!/usr/bin/python3

"""Write a string from a textfile"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file
    returns the number of characters written
    """

    with open(filename, 'w') as f:
        return f.write(text)
