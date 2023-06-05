#!/usr/bin/python3

# Escribe una función que elimine todos los caracteres c y C de una cadena.
def no_c(my_string):
    c_str = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            c_str += i
        
    return(c_str)
