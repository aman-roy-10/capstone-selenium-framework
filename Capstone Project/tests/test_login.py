import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.csv_reader import read_csv

INVALID_LOGINS = read_csv("login_data.csv")


@pytest.mark.smoke
def test_login_page_loads(driver):
    """1. Sanity check: the login/signup page opens and shows both forms."""
    page = LoginPage(driver)
    page.open_page()

    assert "/login" in page.current_url
    assert page.is_loaded(), "Login and signup headings were not displayed"
    assert "login to your account" in page.login_heading_text().lower()
    assert "new user signup" in page.signup_heading_text().lower()
    assert page.login_form_fields_visible(), "Email, password or login button is missing"


@pytest.mark.parametrize("data", INVALID_LOGINS, ids=[row["email"] for row in INVALID_LOGINS])
def test_invalid_login_shows_error(driver, data):
    """2. Wrong credentials (from CSV) show an error message."""
    page = LoginPage(driver)
    page.open_page()
    page.login(data["email"], data["password"])

    assert "incorrect" in page.login_error_text().lower()


def test_valid_login_and_logout(driver, registered_user):
    """Positive case: a real account can log in, sees its name, and can log out.

    The account is created (and deleted afterwards) by the registered_user fixture,
    so no real password is stored in the project.
    """
    page = LoginPage(driver)
    page.open_page()
    page.login(registered_user["email"], registered_user["password"])

    home = HomePage(driver)
    assert home.is_logged_in(), "'Logged in as' was not shown after a valid login"
    assert home.logged_in_username().lower() == registered_user["name"].lower()

    home.logout()
    page.wait_until_on_login_page()
    assert page.is_loaded(), "Login page was not shown after logout"
