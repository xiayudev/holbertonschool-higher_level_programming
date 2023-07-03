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
        self.assertEqual(s1.id, 31)
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
        s1 = Square(10, 0, 0, 50)
        s1_print = "[Square] (50) 0/0 - 10\n"
        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            print(s1)
        assert fake_stdout.getvalue() == s1_print

    def test_update(self):
        """Test for the update method"""
        # test for *args
        r1 = Square(20, 20, 20)
        r1.update(7)
        self.assertEqual(7, r1.id)
        self.assertEqual(20, r1.width)
        self.assertEqual(20, r1.height)
        self.assertEqual(20, r1.x)
        self.assertEqual(20, r1.y)
        r1.update(7, 10, 13, 16)
        self.assertEqual(7, r1.id)
        self.assertEqual(10, r1.width)
        self.assertEqual(10, r1.height)
        self.assertEqual(13, r1.x)
        self.assertEqual(16, r1.y)

        # Test for **kwargs
        r2 = Square(20, 20, 20, 20)
        r2.update(x=2)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 20)
        self.assertEqual(r2.width, 20)
        self.assertEqual(r2.height, 20)
        self.assertEqual(r2.id, 20)
        r2.update(x=3, id=100, height=7, y=4, width=10)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 7)
        self.assertEqual(r2.id, 100)

    def test_save_to_file(self):
        """Test for save to file"""
        s1 = Square(3)
        s2 = Square(5)
        Square.save_to_file([s1, s2])
        file_1 = s1.to_dictionary()
        file_2 = s2.to_dictionary()
        file_ = [file_1, file_2]
        str_json = Rectangle.to_json_string(file_)
        with open("Square.json", "r") as f:
            self.assertEqual(f.readline(), str_json)

        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.readline(), '[]')
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.readline(), '[]')

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
