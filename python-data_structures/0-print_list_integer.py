#!/usr/bin/python3


    # Prototipo: def imprimir_lista_integros(mi_lista=[]):
    # Formato: un entero por línea. Ver ejemplo
    # No puedes importar ningún módulo
    # Puedes asumir que la lista sólo contiene enteros
    # No está permitido convertir enteros en cadenas.
    # Tienes que usar str.format() para imprimir enteros


def print_list_integer(my_list=[]):
        cadena = " ".join(str(num) for num in my_list)
        print(cadena)




