#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.set_size(size)

    def get_size(self):
        """Get the size of the square."""
        return self.__size

    def set_size(self, size):
        """Set the size of the square.

        Args:
            size (int): The new size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

"""
En el código anterior, se definen dos tipos de variables:

1. Tipo de variable: `size` es una variable de tipo entero (`int`).
   - Se utiliza para representar el tamaño del cuadrado.

2. Tipo de variable: `self.__size` es un atributo de instancia de tipo entero (`int`).
   - Es un atributo privado que almacena el tamaño del cuadrado dentro de la clase `Square`.

Valor de las variables:

- Para la variable `size`, el valor se proporciona como argumento al crear una nueva instancia de la clase `Square`. Puede ser cualquier número entero no negativo.
- Para el atributo `self.__size`, el valor se asigna dentro del método `set_size`. Es el valor válido proporcionado como argumento a `set_size`. El valor puede ser cualquier número entero no negativo.

Es importante destacar que `size` es una variable local dentro del método `set_size`, mientras que `self.__size` es un atributo de instancia que se puede acceder desde otros métodos dentro de la clase.
"""