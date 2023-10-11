#!/usr/bin/python3
'''
Class Student
'''


class Student:
    '''
    module of class student
    '''

    def __init__(self, first_name, last_name, age):
        '''
        __init__ method
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        method to_json
        prints all attrs if list is empty
        '''
        if attrs is None:
            return self.__dict__
        else:
            attr_list = {}
            for l in attrs:
                if hasattr(self, l):
                    attr_list[attr] = getattr(self, attr)
            return attr_list
