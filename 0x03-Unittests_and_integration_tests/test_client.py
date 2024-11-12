#!/usr/bin/env python3
"""contains code"""
from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """tests something"""
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch("client.get_json")
    def test_org(self, org, mock):
        """testing"""
        client = GithubOrgClient(org)
        client.org
        mock.called_with_once(client.ORG_URL.format(org=org))
