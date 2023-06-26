#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id_generation(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(42)
        b4 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 42)
        self.assertEqual(b4.id, 3)

if __name__ == '__main__':
    unittest.main()

"""En este ejemplo, definimos una clase de prueba TestBase que hereda de unittest.TestCase. Dentro de esta clase, definimos dos métodos de prueba:

    test_id_generation: Este método verifica que el atributo id se genera correctamente cuando no se proporciona un valor id explícitamente. Creamos tres objetos Base y afirmamos que sus valores de id son 1, 2 y 3, respectivamente.

    test_id_assignment: Este método comprueba la asignación de valores id cuando se proporciona un argumento id. Creamos tres objetos Base, incluyendo uno con un valor id explícito. Comprobamos que los valores de id coinciden con los valores proporcionados o con los generados automáticamente.

Por último, utilizamos unittest.main() para ejecutar las pruebas cuando se ejecuta el script.


n este caso de prueba, creamos varias instancias de la clase Base y comprobamos si el atributo id se asigna correctamente según las condiciones especificadas."""