#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        # test max when in the list 5 is max
        self.assertAlmostEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer(), None)
        self.assertAlmostEqual(max_integer([5, 5, 5, 5, 5]), 5)
    def test_values(self):
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(Exception, max_integer, "Hola")
