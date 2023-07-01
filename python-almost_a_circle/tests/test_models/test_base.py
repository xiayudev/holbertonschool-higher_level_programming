"""Unittest for Base class
"""


import unittest
import json
from modules.base import Base


class TestBase(unittest.TestCase):
    """Testin for a class Base"""

    def test_to_json_string(self):
        """Test for to_json_string"""
        js = json.dumps([{'width': 4, 'height': 5}])

        self.assertEqual(1, Base.id)
        self.assertEqual(12, Base.id)
        self.assertEqual("[]", Base.to_json_string([]))
        self.assertEqual("[]", Base.to_json_string(None))
        self.assertEqual(js, Base.to_json_string([{'width': 4, 'height': 5}]))


if __name__ == '__main__':
    unittest.main()
