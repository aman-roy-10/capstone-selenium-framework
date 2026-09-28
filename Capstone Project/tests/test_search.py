import pytest

from pages.search_page import SearchPage
from utils.csv_reader import read_csv

SEARCH_CASES = read_csv("search_data.csv")


@pytest.mark.parametrize("case", SEARCH_CASES, ids=[c["search_term"] for c in SEARCH_CASES])
def test_product_search(driver, case):
    """5. Data-driven search. Includes a term that must return ZERO results."""
    page = SearchPage(driver)
    page.open_page()
    page.search(case["search_term"])
    count = page.get_result_count()

    if case["expected_result"] == "none":
        assert count == 0, f"Expected zero results for '{case['search_term']}' but got {count}"
    else:
        assert count > 0, f"Expected at least one result for '{case['search_term']}'"
