from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("the user opens the login application")
def step_open_application(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

    context.driver.get("https://www.saucedemo.com/")

    context.wait = WebDriverWait(context.driver, 10)


@when("the user enters valid username and password")
def step_enter_credentials(context):
    username = context.wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )

    password = context.driver.find_element(By.ID, "password")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")


@when("the user clicks the login button")
def step_click_login(context):
    login_button = context.driver.find_element(By.ID, "login-button")
    login_button.click()


@then("the user should be logged in successfully")
def step_verify_login(context):
    inventory_page = context.wait.until(
        EC.visibility_of_element_located((By.ID, "inventory_container"))
    )

    assert inventory_page.is_displayed()

    print("Login successful")


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()