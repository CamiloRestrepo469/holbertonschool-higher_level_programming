#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    if isinstance(a_dictionary, dict):
        max_valor = float("-inf")
        max_clave = None

        for clave, valor in a_dictionary.items():
            if isinstance(valor, int) and valor > max_valor:
                max_valor = valor
                max_clave = clave

        return max_clave
