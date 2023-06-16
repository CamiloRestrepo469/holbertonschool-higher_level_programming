#!/usr/bin/python3
"""_summary_
    """

def text_indentation(text):
    """if text is not None
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    """return indent string"""
    punctuation_marks = ['.', '?', ':']
    
    for delim in punctuation_marks:
        text = delim.join([line.strip(" ") for line in text.split(delim)])
        text = text.replace(delim, delim + "\n\n")

    print(text, end="")

    """
    En esta versión, utilizamos un bucle for para iterar sobre cada marca de puntuación ('.', '?', ':'). Luego, dividimos el texto en líneas usando split(delim), eliminamos los espacios en blanco de cada línea con strip(" ") y finalmente volvemos a unir las líneas con join() usando la marca de puntuación como separador.

Después de eso, utilizamos replace(delim, delim + "\n\n") para reemplazar cada marca de puntuación por la misma marca de puntuación seguida de dos nuevas líneas.

Finalmente, imprimimos el texto resultante utilizando print(text, end="") para evitar un salto de línea adicional al final.

Esta versión logra el mismo resultado que el código original, pero utiliza una sintaxis ligeramente diferente.
    
    """
