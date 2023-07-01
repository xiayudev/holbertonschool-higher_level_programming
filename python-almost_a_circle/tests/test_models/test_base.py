"""Unittest for Base class
"""


import unittest
import json
from models.base import Base


class TestToJsonString(unittest.TestCase):
    """Testin for a class Base"""

    def test_to_json_string_empty(self):
        """Test when Empty list is passed"""
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_None(self):
        """Test when None is passed"""
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string(self):
        """Test when a list of dictionaries is passed"""
        r1 = Base()
        r2 = Base(12)
        js = json.dumps([{'widht': 4, 'height': 5}])
        self.assertEqual(js, Base.to_json_string([{'widht': 4, 'height': 5}]))
        self.assertEqual(str, type(js))
        self.assertEqual(1, r1.id)
        self.assertEqual(12, r2.id)


if __name__ == '__main__':
    unittest.main()
