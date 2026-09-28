from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    SLIDER = (By.ID, "slider")
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")
    PRODUCTS_LINK = (By.CSS_SELECTOR, "a[href='/products']")
    LOGOUT_LINK = (By.CSS_SELECTOR, "a[href='/logout']")
    DELETE_ACCOUNT_LINK = (By.CSS_SELECTOR, "a[href='/delete_account']")
    LOGGED_IN_AS = (By.XPATH, "//a[contains(., 'Logged in as')]/b")
    ACCOUNT_DELETED = (By.CSS_SELECTOR, "h2[data-qa='account-deleted']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a[data-qa='continue-button']")

    def open_home(self):
        self.open("/")

    def is_loaded(self) -> bool:
        return self.is_visible(self.SLIDER, timeout=10)

    def go_to_login(self):
        self.click(self.LOGIN_LINK)

    def go_to_products(self):
        self.click(self.PRODUCTS_LINK)

    def is_logged_in(self) -> bool:
        return self.is_visible(self.LOGGED_IN_AS, timeout=10)

    def logged_in_username(self) -> str:
        return self.get_text(self.LOGGED_IN_AS)

    def logout(self):
        self.click(self.LOGOUT_LINK)

    def logout_if_logged_in(self):
        """Used for clean-up: log out only if a session is active."""
        self.open("/")
        if self.driver.find_elements(*self.LOGOUT_LINK):
            self.click(self.LOGOUT_LINK)

    def delete_account(self):
        self.click(self.DELETE_ACCOUNT_LINK)
        self.find(self.ACCOUNT_DELETED)
        self.click(self.CONTINUE_BUTTON)
