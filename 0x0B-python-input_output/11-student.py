#!/usr/bin/python3

"""
Class Student
"""


class Student:
    """
    Defines a class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        initializes the attributes of class Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        gets the dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__

        else:
            d_list = {}
            for attr in attrs:
                if hasattr(self, attr):
                    d_list[attr] = getattr(self, attr)
            return d_list

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        for keys in json:
            setattr(self, keys, json[keys])
