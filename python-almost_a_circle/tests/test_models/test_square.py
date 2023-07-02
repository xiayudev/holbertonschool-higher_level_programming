"""Unittest for Square class
"""


import unittest
import pycodestyle
import io
from unittest import mock
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Testin for a class Square"""

    def test_to_init(self):
        """Test for the init method"""
        s1 = Square(10)
        self.assertEqual(s1.width, s1.height)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 26)
        self.assertRaises(TypeError, Square, "2")
        self.assertRaises(TypeError, Square, 2, "1")
        self.assertRaises(TypeError, Square, 2, 1, "1")
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(ValueError, Square, 2, -1)
        self.assertRaises(ValueError, Square, 2, 1, -1)
        self.assertRaises(ValueError, Square, 0)
        self.assertIsInstance(Square(10, 2), Rectangle)

    def test_str(self):
        """Test for the __str__ method"""
        s1 = Square(10)
        s1_print = "[Square] (24) 0/0 - 10\n"
        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            print(s1)
        assert fake_stdout.getvalue() == s1_print

    def test_to_dictionary(self):
        """Test for the to_dictionary method"""
        s1 = Square(5, 3, 1)
        s1_dict = s1.to_dictionary()
        self.assertEqual(dict, type(s1_dict))
        self.assertTrue('size' in list(s1_dict))
        self.assertEqual(s1_dict['size'], 5)
        self.assertEqual(s1_dict['x'], 3)
        self.assertEqual(s1_dict['y'], 1)

    def test_pycodestyle_conformance(self):
        """Test for PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/square.py',
                                    'tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0, "Errors")


if __name__ == '__main__':
    unittest.main()
