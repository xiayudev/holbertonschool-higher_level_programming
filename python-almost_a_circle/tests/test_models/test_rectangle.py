"""Unit test for Ractangle class
"""


import unittest
import io
import pycodestyle
from unittest.mock import patch
from unittest import mock
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Ractangle class"""

    def test_to_init(self):
        """Test for the init method"""
        r1 = Rectangle(3, 4)
        self.assertEqual(3, r1.width)
        self.assertEqual(4, r1.height)
        self.assertEqual(0, r1.x)
        self.assertEqual(0, r1.y)
        self.assertEqual(21, r1.id)
        self.assertRaises(TypeError, Rectangle, "3", 4)
        self.assertRaises(TypeError, Rectangle, 3, "4")
        self.assertRaises(ValueError, Rectangle, -1, 3)
        self.assertRaises(ValueError, Rectangle, 1, -3)
        self.assertRaises(ValueError, Rectangle, 0, 3)
        self.assertRaises(ValueError, Rectangle, 2, 0)
        self.assertIsInstance(Rectangle(10, 2), Base)
        r2 = Rectangle(4, 5, 2, 1)
        self.assertEqual(4, r2.width)
        self.assertEqual(5, r2.height)
        self.assertEqual(2, r2.x)
        self.assertEqual(1, r2.y)
        self.assertEqual(23, r2.id)
        self.assertRaises(TypeError, Rectangle, 4, 5, "2", 1)
        self.assertRaises(TypeError, Rectangle, 4, 5, 2, "1")
        self.assertRaises(ValueError, Rectangle, 4, 5, -2, 1)
        self.assertRaises(ValueError, Rectangle, 4, 5, 2, -1)

    def test_area(self):
        """Test for the area method"""
        r1 = Rectangle(3, 2)
        area = r1.area()
        self.assertEqual(area, 6)
        r2 = Rectangle(5, 4, 0, 0, 22)
        area_2 = r2.area()
        self.assertEqual(area_2, 20)

    def test_str(self):
        """Test for the __str__ method"""
        r1 = Rectangle(3, 4, 2, 1, 15)
        rst = "[Rectangle] (15) 2/1 - 3/4\n"
        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            print(r1)
        assert fake_stdout.getvalue() == rst
        r2 = Rectangle(10, 11, 12)
        rst_2 = "[Rectangle] (18) 12/0 - 10/11\n"
        with mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            print(r2)
        assert fake_stdout.getvalue() == rst_2

    def test_update(self):
        """Test for the update method"""
        # test for *args
        r1 = Rectangle(20, 20, 20, 20)
        r1.update(7)
        self.assertEqual(7, r1.id)
        self.assertEqual(20, r1.width)
        self.assertEqual(20, r1.height)
        self.assertEqual(20, r1.x)
        self.assertEqual(20, r1.y)
        r1.update(7, 10, 13, 16, 19)
        self.assertEqual(7, r1.id)
        self.assertEqual(10, r1.width)
        self.assertEqual(13, r1.height)
        self.assertEqual(16, r1.x)
        self.assertEqual(19, r1.y)

        # Test for **kwargs
        r2 = Rectangle(20, 20, 20, 20)
        r2.update(x=2)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 20)
        self.assertEqual(r2.width, 20)
        self.assertEqual(r2.height, 20)
        self.assertEqual(r2.id, 25)
        r2.update(x=3, id=100, height=7, y=4, width=10)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 7)
        self.assertEqual(r2.id, 100)

    def test_to_dictionary(self):
        """Test for the to_dictionary method"""
        r1 = Rectangle(2, 5, 4, 4)
        r1_dict = r1.to_dictionary()
        dict_ = {'width': 2, 'x': 4, 'id': 17, 'height': 5, 'y': 4}
        self.assertEqual(dict, type(r1_dict))
        r2 = Rectangle(10, 10)
        r2.update(**r1_dict)
        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertFalse(r1 == r2)
        self.assertFalse(r1 is r2)

    def test_display(self):
        """Test for the display method"""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(3, 2)
        self.assertEqual(r1.display(), r2.display())

    def test_pycodestyle_conformance(self):
        """Test for PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/rectangle.py',
                                    'tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0, "Found errors")


if __name__ == '__main__':
    unittest.main()
