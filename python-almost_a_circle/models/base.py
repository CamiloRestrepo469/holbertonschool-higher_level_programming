#!/usr/bin/python3
"""create a new Base"""


class Base:
    """Base class for"""

    __nb_objects = 0
    """Number of objects"""

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


"""
 Base:
```
```python
    __nb_objects = 0
```
Esta línea declara un atributo de clase privado llamado `__nb_objects` y lo inicializa con el valor 0. Este atributo se utilizará para contar el número de objetos creados.

```python
    def __init__(self, id=None):
```
Aquí comienza la definición del método especial `__init__`, que es el constructor de la clase. Recibe un argumento llamado `id`, que tiene un valor predeterminado de `None`.

```python
        if id is not None:
            self.id = id
```
Esta declaración condicional verifica si el argumento `id` no es `None`. Si `id` tiene un valor distinto de `None`, se asigna ese valor al atributo de instancia `id`.

```python
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
```
Si el argumento `id` es `None`, se ejecuta el bloque `else`. En este caso, se incrementa el atributo de clase `__nb_objects` en 1 y se asigna ese nuevo valor al atributo de instancia `id`. Esto garantiza que cada objeto tenga un identificador único basado en el número de objetos creados.

En resumen, este código define la clase `Base`, que actúa como una clase base para otras clases. Tiene un atributo de clase privado `__nb_objects` para contar el número de objetos creados y un constructor que asigna un identificador único a cada objeto. Si se proporciona un identificador específico al constructor, se utiliza ese valor; de lo contrario, se genera un identificador basado en la cantidad de objetos creados.


"""