#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def setUp(self):
        pass

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_single_item(self):
        self.assertEqual(max_integer([1]), 1)

    def test_negative_item(self):
        self.assertEqual(max_integer([-1, 0]), 0)

    def test_repeat_items(self):
        self.assertEqual(max_integer([1, -1, 0, 0, 1, -1]), 1)

    def test_all_same(self):
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_descending_list(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

if __name__ == '__main__':
    unittest.testmaxinteger()
