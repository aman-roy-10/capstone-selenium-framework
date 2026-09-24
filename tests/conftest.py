"""Shared PyTest fixtures + the screenshot-on-failure hook."""
import uuid

import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from utils.driver_factory import create_driver
from utils.logger import get_logger
from utils.screenshot import save_screenshot

log = get_logger("tests")

try:  # pytest-html 4.x
    from pytest_html import extras as html_extras
except ImportError:  # pragma: no cover
    html_extras = None


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=None,
                     help="chrome | edge | firefox (default: value in config.ini)")
    parser.addoption("--headless", action="store_true", default=False,
                     help="run without a visible browser window (default: value in config.ini)")


@pytest.fixture(autouse=True)
def _log_test_boundaries(request):
    log.info("START %s", request.node.nodeid)
    yield
    log.info("END   %s", request.node.nodeid)


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = True if request.config.getoption("--headless") else None
    drv = create_driver(browser=browser, headless=headless)
    yield drv
    drv.quit()


@pytest.fixture
def registered_user(driver):
    """Creates a real account, logs out, hands back the credentials, deletes it afterwards.

    Needed by the duplicate-signup test: the site can only say "already exists"
    if the email really is registered.
    """
    name = "Capstone Tester"
    email = f"capstone.{uuid.uuid4().hex[:10]}@example.com"
    password = "Capstone@123"

    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.signup_and_wait(name, email)

    signup_page = SignupPage(driver)
    assert signup_page.is_account_form_displayed(), "Could not reach the account information page"
    signup_page.fill_and_submit(password)
    assert signup_page.is_account_created(), "Account creation did not succeed"
    signup_page.continue_after_creation()

    HomePage(driver).logout()

    yield {"name": name, "email": email, "password": password}

    # Clean-up: never let a clean-up problem fail the test.
    try:
        HomePage(driver).logout_if_logged_in()
        login_page.open_page()
        login_page.login(email, password)
        HomePage(driver).delete_account()
        log.info("Deleted test account %s", email)
    except Exception as error:
        log.warning("Could not delete test account %s: %s", email, error)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """After every test phase: if it failed, save a screenshot and attach it to the HTML report."""
    outcome = yield
    report = outcome.get_result()

    if report.when not in ("setup", "call") or not report.failed:
        return

    drv = item.funcargs.get("driver")
    if drv is None:
        log.error("FAILED %s (%s) - no browser, no screenshot", item.nodeid, report.when)
        return

    path = save_screenshot(drv, item.name)
    log.error("FAILED %s (%s) - screenshot: %s", item.nodeid, report.when, path)
    if html_extras is not None:
        try:
            extra_list = getattr(report, "extras", [])
            extra_list.append(html_extras.png(drv.get_screenshot_as_base64()))
            report.extras = extra_list
        except Exception:
            pass
    if path:
        print(f"\nScreenshot saved: {path}")
