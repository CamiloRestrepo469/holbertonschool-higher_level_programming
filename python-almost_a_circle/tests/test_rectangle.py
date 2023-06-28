import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_valid_width(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.width, 5)

    def test_valid_height(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.height, 10)

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(-5, 10)

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(5, -10)

    def test_invalid_width_type(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle("5", 10)

    def test_invalid_height_type(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(5, "10")

    def test_area(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)

    def test_display(self):
        rectangle = Rectangle(5, 10)
        rectangle.display()  # Manually inspect the output

    def test_to_string(self):
        rectangle = Rectangle(5, 10, id=1, x=2, y=3)
        expected_string = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(rectangle), expected_string)

    def test_update_args(self):
        rectangle = Rectangle(5, 10)
        rectangle.update(2, 7, 15)
        self.assertEqual(rectangle.width, 7)
        self.assertEqual(rectangle.height, 15)

    def test_update_kwargs(self):
        rectangle = Rectangle(5, 10)
        rectangle.update(width=7, height=15)
        self.assertEqual(rectangle.width, 7)
        self.assertEqual(rectangle.height, 15)

if __name__ == '__main__':
    unittest.main()
