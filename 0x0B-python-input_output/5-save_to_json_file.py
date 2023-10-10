#!/usr/bin/python3

'''
function that writes an Object to a text file, using a JSON representation
'''

import json
"""provide functions needed to convert"""



def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file,
    using a JSON representation:
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
