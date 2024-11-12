#!/usr/bin/env python3
"""testing access to nested map"""

import unittest
from parameterized import parameterized
import utils


class TestAccessNestedMap(unittest.TestCase):
    """Test the access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)

    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access to nested map"""
        result = utils.access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test access to nested map with exception"""
        with self.assertRaises(KeyError) as err:
            utils.access_nested_map(nested_map, path)

        self.assertEqual(f"KeyError('{expected}')", repr(err.exception))
