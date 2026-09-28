"""BasePage: shared helpers used by every page object."""
import time

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from utils import config_reader
from utils.logger import get_logger


class BasePage:
    CONSENT_BUTTON = (By.CSS_SELECTOR, "button.fc-cta-consent")

    def __init__(self, driver):
        self.driver = driver
        self.base_url = config_reader.get_base_url()
        self.wait = WebDriverWait(driver, config_reader.get_explicit_wait())
        self.log = get_logger(self.__class__.__name__)

    # ---------- navigation ----------
    def open(self, path: str = "/"):
        self.log.info("Open %s%s", self.base_url, path)
        self.driver.get(self.base_url + path)
        self._dismiss_consent_popup()
        self._remove_ads()

    def _dismiss_consent_popup(self):
        """The site shows a cookie-consent dialog on the first visit. Close it if present."""
        try:
            button = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(self.CONSENT_BUTTON))
            button.click()
            self.log.info("Closed cookie-consent popup")
        except Exception:
            pass  # popup not shown - nothing to do

    def _remove_ads(self):
        """Best effort: delete ad frames so they cannot cover buttons."""
        try:
            self.driver.execute_script(
                "document.querySelectorAll("
                "'ins.adsbygoogle, iframe[id^=\"aswift\"], iframe[id^=\"google_ads\"]')"
                ".forEach(e => e.remove());"
            )
        except Exception:
            pass

    @property
    def current_url(self) -> str:
        return self.driver.current_url

    @property
    def title(self) -> str:
        return self.driver.title

    # ---------- element helpers ----------
    def find(self, locator):
        """Wait until the element is visible, then return it."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Normal click; if an ad floats over the button, fall back to a JavaScript click.

        KNOWN ISSUE #1: Google ads on automationexercise.com can cover buttons and cause
        ElementClickInterceptedException. A JavaScript click ignores whatever is on top.
        """
        self.log.info("Click %s", locator[1])
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except (ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException):
            self.log.warning("Normal click blocked on %s - using JavaScript click", locator[1])
            element = self.driver.find_element(*locator)  # re-find in case the page re-rendered
            self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, text: str):
        # Never write passwords into the log file.
        shown = "****" if "password" in str(locator[1]).lower() else text
        self.log.info("Type '%s' into %s", shown, locator[1])
        element = self.find(locator)
        element.clear()
        if text:
            element.send_keys(text)

    def get_text(self, locator) -> str:
        return self.find(locator).text.strip()

    def select_by_text(self, locator, text: str):
        Select(self.find(locator)).select_by_visible_text(text)

    def select_by_value(self, locator, value: str):
        Select(self.find(locator)).select_by_value(value)

    def is_visible(self, locator, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_field_valid(self, locator) -> bool:
        """Uses the browser's built-in HTML5 validation (required / type=email)."""
        element = self.driver.find_element(*locator)
        return bool(self.driver.execute_script("return arguments[0].validity.valid;", element))

    @staticmethod
    def pause(seconds: float):
        time.sleep(seconds)
