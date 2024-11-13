#!/usr/bin/env python3
"""some code"""
from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch, PropertyMock


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

    def test_public_repos_url(self):
        "does something too"
        with patch.object(
                GithubOrgClient,
                "org",
                new_callable=PropertyMock
        )as mocked_object:

            mocked_object.return_value = {"repos_url": "salut_bb"}
            haja = GithubOrgClient("staghferallah")
            natija = haja._public_repos_url
            self.assertEqual(natija, mocked_object.return_value["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mocked_get):
        """coming soon"""
        payload = [{"name": "loay"}, {"name": "abassi"}]
        mocked_get.return_value = payload
        with patch(
            "client.GithubOrgClient._public_repos_url"
        ) as mocking_public:
            mocking_public.return_value = payload
            simulation = GithubOrgClient("endpoint")
            result = simulation._public_repos_url()
            expectation = [p["name"] for p in payload]
            self.assertEqual(result, expectation)
        mocked_get.assert_called_once()
        mocking_public.assert_called_once()

    parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])

    def test_has_license(self, repo, license_key, expected):
        """license w master..."""
        result = GithubOrgClient("test")
        self.assertEqual(result.has_license(repo, license_key, expected))


if __name__ == "__main__":
    unittest.main()
