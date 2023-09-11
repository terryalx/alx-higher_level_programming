#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    element_a = tuple_a + (0, 0)
    element_b = tuple_b + (0, 0)

    results1 = 0
    results2 = 0

    results1 += element_a[0] + element_b[0]
    results2 += element_a[1] + element_b[1]

    return (results1, results2)
