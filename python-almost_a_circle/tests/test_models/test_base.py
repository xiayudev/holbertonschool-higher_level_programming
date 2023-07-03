"""Unittest for Base class
"""


import unittest
import json
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Testin for a class Base"""

    def test_to_init(self):
        """Test for the init method"""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        b4 = Base(None)
        self.assertEqual(16, b1.id)
        self.assertEqual(12, b2.id)
        self.assertEqual(17, b3.id)
        self.assertEqual(18, b4.id)
        self.assertEqual(Base("3").id, "3")
        b1.id = 45
        self.assertEqual(45, b1.id)
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_to_json_string(self):
        """Test for the to_json_string method"""
        self.assertEqual("[]", Base.to_json_string([]))
        self.assertEqual("[]", Base.to_json_string(None))
        js = json.dumps([{'widht': 4, 'height': 5}])
        self.assertEqual(js, Base.to_json_string([{'widht': 4, 'height': 5}]))
        self.assertEqual(str, type(js))

    def test_from_json_string(self):
        """Test for the from_json_string method"""
        str_json = '[{"widht": 4, "height": 5}]'
        self.assertEqual([], Base.from_json_string(""))
        self.assertEqual([], Base.from_json_string(None))
        js = json.loads(str_json)
        self.assertEqual(js, Base.from_json_string(str_json))
        self.assertEqual(list, type(js))

    def test_save_to_file(self):
        """Test for the save_to_file method"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.readline(), '[]')

        # Working with a list of Rectangle objects
        r1 = Rectangle(3, 4)
        r2 = Rectangle(5, 4)
        Rectangle.save_to_file([r1, r2])
        file_1 = r1.to_dictionary()
        file_2 = r2.to_dictionary()
        file_ = [file_1, file_2]
        str_json = Rectangle.to_json_string(file_)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.readline(), str_json)

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.readline(), '[]')

        Rectangle.save_to_file([1, 2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.readline(), '[{}, {}]')

    def test_create(self):
        """Test for create method"""
        r1 = Rectangle(3, 5, 1)
        r1_d = r1.to_dictionary()
        r2 = Rectangle.create(**r1_d)
        self.assertAlmostEqual(r1.id, 1)
        self.assertAlmostEqual(r2.id, 1)
        self.assertAlmostEqual(r2.width, 3)
        self.assertAlmostEqual(r2.height, 5)
        self.assertAlmostEqual(r2.x, 1)
        self.assertAlmostEqual(r2.y, 0)
        self.assertFalse(r1 == r2)
        self.assertFalse(r1 is r2)
        r4 = Rectangle(3, 5, 1, 2, 7)
        r4_dictionary = r4.to_dictionary()
        r5 = Rectangle.create(**r4_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r5))

    def test_load_from_file(self):
        """Test for test_load_from_file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_input = [r1, r2]
        Rectangle.save_to_file(list_input)
        list_output = Rectangle.load_from_file()
        self.assertAlmostEqual(list_output[0].id, 4)
        self.assertAlmostEqual(list_output[0].x, 2)
        self.assertAlmostEqual(list_output[0].width, 10)
        self.assertAlmostEqual(list_output[0].height, 7)
        self.assertAlmostEqual(list_output[0].y, 8)
        self.assertAlmostEqual(list_output[1].id, 5)
        self.assertAlmostEqual(list_output[1].x, 0)
        self.assertAlmostEqual(list_output[1].width, 2)
        self.assertAlmostEqual(list_output[1].height, 4)
        self.assertAlmostEqual(list_output[1].y, 0)
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        sinput = [s1, s2]
        Square.save_to_file(sinput)
        soutput = Square.load_from_file()
        self.assertAlmostEqual(soutput[0].id, 8)
        self.assertAlmostEqual(soutput[0].width, 5)
        self.assertAlmostEqual(soutput[0].height, 5)
        self.assertAlmostEqual(soutput[0].x, 0)
        self.assertAlmostEqual(soutput[0].y, 0)
        self.assertAlmostEqual(soutput[1].id, 9)
        self.assertAlmostEqual(soutput[1].width, 7)
        self.assertAlmostEqual(soutput[1].height, 7)
        self.assertAlmostEqual(soutput[1].x, 9)
        self.assertAlmostEqual(soutput[1].y, 1)
        ########
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_pycodestyle_conformance(self):
        """Test for PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base.py',
                                    'tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0, "Found errors")


if __name__ == '__main__':
    unittest.main()
