#!/usr/bin/python3
"""Unittest for Base class
"""


import unittest
import json
from modules.base import Base


class TestBase(unittest.TestCase):
    """Testin for a class Base"""

    def test_to_json_string(self):
        b1 = Base()
        js = json.dumps([{'width': 4, 'height': 5}])

        self.assertEqual(b1.id, 1)
        self.assertEqual(b1.to_json_string([]), "[]")
        self.assertEqual(b1.to_json_string(None), "[]")
        self.assertEqual(b1.to_json_string([{'width': 4, 'height': 5}]), js)

if __name__=='__main__':
	unittest.main()
