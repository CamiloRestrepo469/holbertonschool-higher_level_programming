#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    # Verificar si se pasaron argumentos
    if len(sys.argv) > 1:
        # Inicializar la variable de suma en cero
        suma = 0

        # Iterar sobre los argumentos, comenzando desde el segundo elemento
        for argument in sys.argv[1:]:
            # Convertir el argumento a entero y sumarlo a la variable
            suma += int(argument)

        # Imprimir el resultado de la suma
        print(suma)
    else:
        print(0)

