import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        r = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 1)

    def test_width_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle("invalid", 10, 2, 3, 1)
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 10, 2, 3, 1)

    def test_height_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, "invalid", 2, 3, 1)
        with self.assertRaises(ValueError):
            r = Rectangle(5, -10, 2, 3, 1)

    def test_x_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, "invalid", 3, 1)
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, -2, 3, 1)

    def test_y_validation(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, 2, "invalid", 1)
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, 2, -3, 1)

    def test_area(self):
        r = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        r = Rectangle(4, 6, 2, 2)
        expected_output = "  ##\n  ##\n  ##\n  ##\n  ##\n  ##\n"
        self.assertEqual(self.capture_stdout(r.display), expected_output)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 2)
        self.assertEqual(r.width, 2)
        r.update(89, 2, 3)
        self.assertEqual(r.height, 3)
        r.update(89, 2, 3, 4)
        self.assertEqual(r.x, 4)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(r.height, 1)
        r.update(width=1, x=2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.x, 2)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.id, 89)
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.width, 4)

    def capture_stdout(self, function):
        import sys
        from io import StringIO

        stdout = sys.stdout
        sys.stdout = StringIO()
        function()
        output = sys.stdout.getvalue()
        sys.stdout = stdout
        return output


if __name__ == "__main__":
    unittest.main()
