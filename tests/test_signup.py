import pytest

from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from utils.csv_reader import read_csv

SIGNUP_USERS = read_csv("signup_users.csv")
VALIDATION_CASES = read_csv("signup_validation_data.csv")


@pytest.mark.parametrize("user", SIGNUP_USERS, ids=[u["email"] for u in SIGNUP_USERS])
def test_new_user_signup_form(driver, user):
    """3. A new name + email moves on to the 'Enter Account Information' page."""
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.signup_and_wait(user["name"], user["email"])

    signup_page = SignupPage(driver)
    assert signup_page.is_account_form_displayed(), (
        "Did not reach the account information page. If the site said the email already "
        "exists, change it in data/signup_users.csv (use a different dot-alias)."
    )


def test_duplicate_signup_shows_error(driver, registered_user):
    """4. Signing up again with an already-registered email shows an error."""
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.signup_and_wait(registered_user["name"], registered_user["email"])

    assert "already exist" in login_page.signup_error_text().lower()


@pytest.mark.parametrize("case", VALIDATION_CASES, ids=[c["case_id"] for c in VALIDATION_CASES])
def test_signup_validation(driver, case):
    """6. Missing name / bad email formats are blocked by the form (data from CSV)."""
    page = LoginPage(driver)
    page.open_page()
    page.signup(case["name"], case["email"])

    assert page.still_on_login_page(), "Form was accepted but should have been blocked"
    assert not page.signup_field_is_valid(case["invalid_field"]), (
        f"Expected the '{case['invalid_field']}' field to be invalid"
    )
