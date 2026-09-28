from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class LoginPage(BasePage):
    PATH = "/login"

    # Login form (left side)
    LOGIN_HEADING = (By.CSS_SELECTOR, ".login-form h2")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGIN_ERROR = (By.CSS_SELECTOR, ".login-form p")

    # Signup form (right side)
    SIGNUP_HEADING = (By.CSS_SELECTOR, ".signup-form h2")
    SIGNUP_NAME = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    SIGNUP_EMAIL = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    SIGNUP_ERROR = (By.CSS_SELECTOR, ".signup-form p")

    def open_page(self):
        self.open(self.PATH)

    # ---------- checks ----------
    def is_loaded(self) -> bool:
        return (
            self.is_visible(self.LOGIN_HEADING, timeout=10)
            and self.is_visible(self.SIGNUP_HEADING, timeout=10)
        )

    def login_heading_text(self) -> str:
        return self.get_text(self.LOGIN_HEADING)

    def signup_heading_text(self) -> str:
        return self.get_text(self.SIGNUP_HEADING)

    def login_form_fields_visible(self) -> bool:
        return all(self.is_visible(loc, timeout=3) for loc in
                   (self.LOGIN_EMAIL, self.LOGIN_PASSWORD, self.LOGIN_BUTTON))

    # ---------- actions ----------
    def login(self, email: str, password: str):
        self.type(self.LOGIN_EMAIL, email)
        self.type(self.LOGIN_PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def signup(self, name: str, email: str):
        self.type(self.SIGNUP_NAME, name)
        self.type(self.SIGNUP_EMAIL, email)
        self.click(self.SIGNUP_BUTTON)

    def signup_and_wait(self, name: str, email: str, attempts: int = 3):
        """Signup that survives the site's random ad interstitials.

        Sometimes an ad "swallows" the click: no error is raised but the form is never
        submitted (URL becomes /login#google_vignette). After each click we wait for the
        result - the /signup page OR the on-page error message. If neither appears,
        the page is reloaded and the signup is tried again.
        """
        for attempt in range(1, attempts + 1):
            if attempt > 1:
                self.log.warning("Signup did not go through (attempt %d) - reloading and retrying", attempt - 1)
                self.open_page()
            self.signup(name, email)
            try:
                WebDriverWait(self.driver, 8).until(
                    lambda d: "/signup" in d.current_url or d.find_elements(*self.SIGNUP_ERROR)
                )
                return
            except TimeoutException:
                continue

    def login_error_text(self) -> str:
        return self.get_text(self.LOGIN_ERROR)

    def signup_error_text(self) -> str:
        return self.get_text(self.SIGNUP_ERROR)

    def signup_field_is_valid(self, field: str) -> bool:
        """field is 'name' or 'email'."""
        locator = self.SIGNUP_NAME if field == "name" else self.SIGNUP_EMAIL
        return self.is_field_valid(locator)

    def still_on_login_page(self) -> bool:
        return "/login" in self.current_url

    def wait_until_on_login_page(self):
        """Wait for the redirect to /login (e.g. after logging out)."""
        self.wait.until(lambda d: "/login" in d.current_url)
