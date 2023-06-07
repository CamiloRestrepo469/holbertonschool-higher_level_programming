#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    lista = []
    for row in matrix:
        two_list = []
        for col in row:
            two_list.append(col ** 2)
        lista.append(two_list)
    return lista

