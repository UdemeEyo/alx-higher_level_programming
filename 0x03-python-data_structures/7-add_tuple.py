#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    len_a = len(tuple_a)
    len_b = len(tuple_b)
    add_tup = ()

    for i in range(2):
        if i >= len_a:
            a = 0
        else:
            a = tuple_a[i]
        if i >= len_b:
            b = 0
        else:
            b = tuple_b[i]

        if (i == 0):
            add_tup = a + b
        else:
            add_tup = (add_tup, a + b)
    return (add_tup)
