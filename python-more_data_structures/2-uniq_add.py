#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set(my_list)
    # Convertir la lista en un conjunto
    # para eliminar duplicados
    sum_result = sum(unique_integers)
    # Sumar todos los enteros
    # únicos del conjunto
    return sum_result
