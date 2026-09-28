"""The 'Enter Account Information' page shown after a valid signup."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SignupPage(BasePage):
    PASSWORD = (By.ID, "password")
    DAYS = (By.ID, "days")
    MONTHS = (By.ID, "months")
    YEARS = (By.ID, "years")
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    ADDRESS = (By.ID, "address1")
    COUNTRY = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE = (By.ID, "mobile_number")
    CREATE_ACCOUNT = (By.CSS_SELECTOR, "button[data-qa='create-account']")
    ACCOUNT_CREATED = (By.CSS_SELECTOR, "h2[data-qa='account-created']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a[data-qa='continue-button']")

    def is_account_form_displayed(self) -> bool:
        return "/signup" in self.current_url and self.is_visible(self.PASSWORD, timeout=10)

    def fill_and_submit(self, password: str):
        self.type(self.PASSWORD, password)
        self.select_by_value(self.DAYS, "1")
        self.select_by_value(self.MONTHS, "1")
        self.select_by_value(self.YEARS, "1995")
        self.type(self.FIRST_NAME, "Capstone")
        self.type(self.LAST_NAME, "Tester")
        self.type(self.ADDRESS, "1 Test Street")
        self.select_by_text(self.COUNTRY, "India")
        self.type(self.STATE, "West Bengal")
        self.type(self.CITY, "Kolkata")
        self.type(self.ZIPCODE, "700001")
        self.type(self.MOBILE, "9999999999")
        self.click(self.CREATE_ACCOUNT)

    def is_account_created(self) -> bool:
        return self.is_visible(self.ACCOUNT_CREATED, timeout=15)

    def continue_after_creation(self):
        self.click(self.CONTINUE_BUTTON)
