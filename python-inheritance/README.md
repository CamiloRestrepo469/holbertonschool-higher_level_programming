## herencia de clase

1. Superclase, Clase Base o Clase Padre:
   - Una superclase, clase base o clase padre es una clase de la cual otra clase hereda atributos y métodos. Proporciona una base común para las clases derivadas (subclases) y puede contener implementaciones y comportamientos generales que se comparten entre las subclases.

2. Subclase:
   - Una subclase es una clase que hereda atributos y métodos de una superclase o clase base. La subclase puede agregar atributos y métodos adicionales o modificar los existentes heredados de la superclase.

3. Enumerar atributos y métodos de una clase o instancia:
   - Para enumerar todos los atributos y métodos de una clase, puedes utilizar la función `dir(Clase)`. Esto devolverá una lista de los nombres de los atributos y métodos disponibles.
   - Para enumerar los atributos y métodos de una instancia específica, puedes utilizar `dir(instancia)`.

4. Instancias con nuevos atributos:
   - Una instancia puede tener nuevos atributos asignados dinámicamente utilizando la notación de punto. Puedes asignar un nuevo valor a un atributo existente o crear uno completamente nuevo directamente en la instancia.

5. Herencia de una clase:
   - Para heredar una clase de otra, simplemente especifica la clase base entre paréntesis después del nombre de la clase derivada. Por ejemplo: `class ClaseDerivada(ClaseBase):`

6. Definición de una clase con múltiples clases base:
   - Para definir una clase con múltiples clases base, simplemente enumera las clases base separadas por comas dentro de los paréntesis después del nombre de la clase derivada. Por ejemplo: `class ClaseDerivada(ClaseBase1, ClaseBase2):`

7. Clase por defecto de la que hereda cada clase:
   - En Python, si no se especifica explícitamente una superclase, todas las clases heredan implícitamente de la clase base `object`. Por lo tanto, la clase `object` es la clase por defecto de la que heredan todas las demás clases.

8. Anulación de un método o atributo heredado:
   - Para anular un método o atributo heredado de la clase base, simplemente define el mismo método o atributo en la clase derivada. La implementación en la clase derivada reemplazará la implementación heredada de la clase base.

9. Atributos o métodos disponibles por herencia para las subclases:
   - Las subclases heredan todos los atributos y métodos públicos (no precedidos por doble guión bajo) de la clase base, incluidos los métodos y atributos heredados de las superclases de la clase base.

10. Propósito de la herencia:
    - La herencia permite la reutilización de código y la creación de jerarquías de clases. Permite que las clases hereden características comunes de una clase base, evitando la duplicación de código y facilitando la organización y estructura de programas orientados a objetos.

11. Funciones `isinstance`, `issubclass`, `type` y `super`:
    - La función `isinstance(objeto, Clase)` devuelve `True` si el objeto es una instancia de la clase (o

 una subclase de la clase), de lo contrario, devuelve `False`.
    - La función `issubclass(ClaseDerivada, ClaseBase)` devuelve `True` si la clase derivada es una subclase de la clase base, de lo contrario, devuelve `False`.
    - La función `type(objeto)` devuelve el tipo de objeto, que es esencialmente la clase de la que se creó el objeto.
    - La función `super()` devuelve un objeto proxy especial que permite llamar a los métodos de la superclase en la jerarquía de herencia. Se utiliza para acceder y llamar a métodos heredados desde una clase derivada.

Espero que esta información sea útil para tu blog. Si tienes más preguntas, ¡no dudes en preguntar!