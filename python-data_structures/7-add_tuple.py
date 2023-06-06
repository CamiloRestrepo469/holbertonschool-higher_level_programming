#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Fill missing elements with 0 if tuple length is less than 2
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))

    # Take only the first 2 elements of each tuple
    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]

    # Perform element-wise addition of the tuples
    sum_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return sum_tuple
