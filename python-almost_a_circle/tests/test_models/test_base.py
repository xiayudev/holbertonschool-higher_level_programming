"""Unittest for Base class
"""


import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):
    """Testin for a class Base"""

    def test_to_init(self):
        """Test for the init method"""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(1, b1.id)
        self.assertEqual(12, b2.id)
        self.assertEqual(2, b3.id)

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


if __name__ == '__main__':
    unittest.main()
