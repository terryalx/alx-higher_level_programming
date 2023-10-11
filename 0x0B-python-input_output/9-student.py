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

    def to_json(self):
        '''
        method to_json
        print __dict__ of Student instance
        '''
        return self.__dict__
