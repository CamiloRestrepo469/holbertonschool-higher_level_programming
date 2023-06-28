#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_base_id_auto_increment(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_base_id_specified(self):
        base = Base(89)
        self.assertEqual(base.id, 89)

    def test_to_json_string_none(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, '[]')

    def test_to_json_string_empty_list(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, '[]')

    def test_to_json_string_list_with_id(self):
        json_string = Base.to_json_string([{'id': 12}])
        self.assertEqual(json_string, '[{"id": 12}]')

    def test_from_json_string_none(self):
        obj_list = Base.from_json_string(None)
        self.assertEqual(obj_list, [])

    def test_from_json_string_empty_string(self):
        obj_list = Base.from_json_string("[]")
        self.assertEqual(obj_list, [])

    def test_from_json_string_list_with_id(self):
        obj_list = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(obj_list, [{'id': 89}])

if __name__ == '__main__':
    unittest.main()



"""En este ejemplo, definimos una clase de prueba TestBase que hereda de unittest.TestCase. Dentro de esta clase, definimos dos métodos de prueba:

    test_id_generation: Este método verifica que el atributo id se genera correctamente cuando no se proporciona un valor id explícitamente. Creamos tres objetos Base y afirmamos que sus valores de id son 1, 2 y 3, respectivamente.

    test_id_assignment: Este método comprueba la asignación de valores id cuando se proporciona un argumento id. Creamos tres objetos Base, incluyendo uno con un valor id explícito. Comprobamos que los valores de id coinciden con los valores proporcionados o con los generados automáticamente.

Por último, utilizamos unittest.main() para ejecutar las pruebas cuando se ejecuta el script.


n este caso de prueba, creamos varias instancias de la clase Base y comprobamos si el atributo id se asigna correctamente según las condiciones especificadas."""