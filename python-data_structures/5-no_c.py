#!/usr/bin/python3

# Escribe una función que elimine todos los caracteres c y C de una cadena.
def no_c(my_string):
    c = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            c += i
        
        return(c)
