#!/usr/bin/python3
'''
Write a class MyList that inherits from list
'''


class MyList(list):
    ''' Represents a MyList'''

    def print_sorted(self):
        '''
        prints a sorted list
        '''
        print(sorted(self))
