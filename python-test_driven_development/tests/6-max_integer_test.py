#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def tex_max_integer(self):
        self.assertEqual(max_integer(5, 7), 12)
        

if __name__ == '__main__':
    unittest.main()
        