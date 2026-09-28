from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='search']")
    SEARCH_BUTTON = (By.ID, "submit_search")

    PRODUCT_NAMES = (
        By.XPATH,
        "//div[contains(@class,'productinfo')]//p"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def search_product(self, product_name):
        search_box = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )

        search_box.clear()
        search_box.send_keys(product_name)

        search_button = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )

        search_button.click()

    def get_product_names(self):
        elements = self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCT_NAMES)
        )

        return [element.text for element in elements]