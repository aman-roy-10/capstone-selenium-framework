"""Product search tests using unittest, with data from data/search_data.csv."""
import unittest

from legacy_unittest.base_test import BaseUnittest
from pages.search_page import SearchPage
from utils.csv_reader import read_csv


def _first_row(expected: str) -> dict:
    return next(row for row in read_csv("search_data.csv") if row["expected_result"] == expected)


class SearchUnittest(BaseUnittest):

    def setUp(self):
        self.page = SearchPage(self.driver)
        self.page.open_page()

    def test_search_returns_results(self):
        term = _first_row("found")["search_term"]
        self.page.search(term)
        self.assertGreater(self.page.get_result_count(), 0, f"No results for '{term}'")

    def test_search_with_no_match_returns_zero(self):
        term = _first_row("none")["search_term"]
        self.page.search(term)
        self.assertEqual(self.page.get_result_count(), 0, f"Expected zero results for '{term}'")


if __name__ == "__main__":
    unittest.main()
