#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    # Variable para realizar un seguimiento
    # del número de elementos impresos

    try:
        for i in range(x):
            # Iterar sobre los primeros "x"
            # elementos de la lista
            print(my_list[i], end="")
            # Imprimir el elemento sin
            # un salto de línea
            count += 1
            # Incrementar el
            # contador de elementos impresos

    except IndexError:
        # Capturar la excepción IndexError
        # en caso de que "x" sea mayor que
        # la longitud de la lista
        pass
    # No hacer nada en caso de excepción

    print("")
    # Imprimir un salto de línea después
    # de imprimir los elementos
    return count
# Devolver el número real de elementos impresos
