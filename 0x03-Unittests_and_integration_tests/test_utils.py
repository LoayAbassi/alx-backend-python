#!/usr/bin/env python3
"""testing access to nested map"""
from unittest.mock import patch, Mock
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


class TestGetJson(unittest.TestCase):
    """mocking http calls"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})

    ])
    def test_get_json(self, test_url, test_payload):
        """testing get json method"""
        with patch("utils.requests.get") as mocked_get:
            mocked_response = Mock()
            mocked_response.json.return_value = test_payload
            mocked_get.return_value = mocked_response

            result = utils.get_json(test_url)
            mocked_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)
