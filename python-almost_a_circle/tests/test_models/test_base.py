#!/usr/bin/python3
"""Unittest for Base class
"""


import unittest
import json
from modules.base import Base.to_json_string


class TestToJsonString(unittest.TestCase):
    """Testin for a class Base"""

    def test_to_json_string(self):
        x = Base(4, 5)
        js = json.dumps([{'width': 4, 'height': 5}])
        self.assertEqual(to_json_string([]), "[]")
        self.assertEqual(to_json_string(None), "[]")
        self.assertEqual(to_json_string([{'width': 4, 'height': 5}]), js)
        self.assertRaises(Exception, to_json_string(5))
        self.assertRaises(Exception, to_json_string("5"))
        self.assertRaises(Exception, to_json_string(x))
