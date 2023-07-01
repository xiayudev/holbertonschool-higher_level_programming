#!/usr/bin/python3
"""Unittest for Base class
"""


import unittest
import json
from modules.base import Base


class TestBase(unittest.TestCase):
    """Testin for a class Base"""

    def test_to_json_string(self):
        x = Base(4, 5)
        js = json.dumps([{'width': 4, 'height': 5}])
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([{'width': 4, 'height': 5}]), js)
        self.assertRaises(Exception, Base.to_json_string(5))
        self.assertRaises(Exception, Base.to_json_string("5"))
        self.assertRaises(Exception, Base.to_json_string(x))
