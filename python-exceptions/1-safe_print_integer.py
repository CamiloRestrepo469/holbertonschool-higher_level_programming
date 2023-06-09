#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        # Imprimir el valor como entero
        # utilizando el formato "{:d}"
        return True
    # Devolver True si el valor
    # es un entero y se imprime correctamente
    except (ValueError, TypeError):
        # Capturar cualquier excepción que
        # pueda ocurrir durante la impresión
        return False
    # Devolver False si se produce
    # una excepción, lo que indica que el valor
    # no es un entero o no se puede imprimir como entero
