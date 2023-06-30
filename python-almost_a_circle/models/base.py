#!/usr/bin/python3
"""import json"""
import json
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

    """static method"""
    @staticmethod
    def to_json_string(list_dictionaries):
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    """class method"""
    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dict = [o.to_dictionary() for o in list_objs]
                json_file.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        import json
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
    

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy instance of Rectangle with default values
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy instance of Square with default values
        else:
            dummy = cls()  # Create a dummy instance of the class with no default values

        dummy.update(**dictionary)  # Use the update method to set the attributes from the dictionary
        return dummy
    
    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"  # Filename based on class name
        try:
            with open(filename, "r") as file:
                json_data = file.read()  # Read the JSON data from the file
                dictionaries = cls.from_json_string(json_data)  # Convert JSON to list of dictionaries
                instances = [cls.create(**d) for d in dictionaries]  # Create instances from dictionaries
                return instances
        except FileNotFoundError:
            return []



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
