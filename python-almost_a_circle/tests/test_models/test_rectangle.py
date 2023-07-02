"""Unit test for Ractangle class
"""


import unittest
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
        self.assertEqual(15, r1.id)
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
        self.assertEqual(17, r2.id)
        self.assertRaises(TypeError, Rectangle, 4, 5, "2", 1)
        self.assertRaises(TypeError, Rectangle, 4, 5, 2, "1")
        self.assertRaises(ValueError, Rectangle, 4, 5, -2, 1)
        self.assertRaises(ValueError, Rectangle, 4, 5, 2, -1)


if __name__ == '__main__':
    unittest.main()
