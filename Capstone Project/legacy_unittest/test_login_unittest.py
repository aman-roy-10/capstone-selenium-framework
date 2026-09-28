"""Login tests using Python's built-in unittest (NOT collected by PyTest).

Run from the project root:
    python -m legacy_unittest.run_suite          (also writes an HTML report)
    python -m unittest discover -s legacy_unittest -t . -v
"""
import unittest

from legacy_unittest.base_test import BaseUnittest
from pages.login_page import LoginPage
from utils.csv_reader import read_csv


class LoginUnittest(BaseUnittest):

    def setUp(self):
        self.page = LoginPage(self.driver)
        self.page.open_page()

    def test_login_page_loads(self):
        self.assertIn("/login", self.page.current_url)
        self.assertTrue(self.page.is_loaded())
        self.assertIn("login to your account", self.page.login_heading_text().lower())

    def test_invalid_login_shows_error(self):
        creds = read_csv("login_data.csv")[0]
        self.page.login(creds["email"], creds["password"])
        self.assertIn("incorrect", self.page.login_error_text().lower())


if __name__ == "__main__":
    unittest.main()
