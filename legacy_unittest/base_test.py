"""Shared base class for the Unittest suite (browser start/stop + screenshot on failure)."""
import unittest

from utils.driver_factory import create_driver
from utils.logger import get_logger
from utils.screenshot import save_screenshot

log = get_logger("unittest")


class BaseUnittest(unittest.TestCase):
    driver = None
    screenshot_path = None  # filled in when this test fails

    @classmethod
    def setUpClass(cls):
        cls.driver = create_driver()

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.quit()

    def run(self, result=None):
        """Wrap the normal run so we can log it and take a screenshot when the test fails."""
        if result is None:
            result = self.defaultTestResult()
        log.info("START %s", self.id())
        before = len(getattr(result, "failures", [])) + len(getattr(result, "errors", []))
        outcome = super().run(result)
        after = len(getattr(result, "failures", [])) + len(getattr(result, "errors", []))
        if after > before:
            self.screenshot_path = save_screenshot(self.driver, self.id())
            log.error("FAILED %s - screenshot: %s", self.id(), self.screenshot_path)
        log.info("END   %s", self.id())
        return outcome
