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


if __name__ == '__main__':
    unittest.main()
