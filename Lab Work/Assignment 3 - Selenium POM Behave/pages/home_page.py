from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    URL = "https://automationexercise.com/"

    PRODUCTS_LINK = (
        By.XPATH,
        "//a[contains(@href, '/products')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def click_products(self):
        products_link = self.wait.until(
            EC.element_to_be_clickable(self.PRODUCTS_LINK)
        )
        products_link.click()