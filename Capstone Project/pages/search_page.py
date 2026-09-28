import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchPage(BasePage):
    PATH = "/products"

    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    HEADING = (By.CSS_SELECTOR, ".features_items h2.title")
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".features_items .product-image-wrapper")

    def open_page(self):
        self.open(self.PATH)

    def search(self, term: str):
        self.type(self.SEARCH_INPUT, term)
        self.click(self.SEARCH_BUTTON)  # click() has the JS fallback for ad interception
        # The "Searched Products" heading appears even when there are 0 matches,
        # so it is a safe thing to wait for.
        self.wait.until(lambda d: "searched products" in d.find_element(*self.HEADING).text.lower())

    def get_result_count(self) -> int:
        # KNOWN ISSUE #2 (zero-results wait bug): do NOT use a waiting helper such as
        # presence_of_all_elements_located here. A search with zero matches correctly has
        # no product cards, so that wait would run until it times out and throw
        # TimeoutException. Instead: a short fixed pause to let the results render, then a
        # direct find_elements() call, which simply returns an empty list when nothing matches.
        time.sleep(1)
        count = len(self.driver.find_elements(*self.PRODUCT_CARDS))
        self.log.info("Search returned %d product(s)", count)
        return count
