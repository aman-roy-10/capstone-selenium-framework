import json
import os

from behave import given, when, then
from selenium import webdriver

from pages.home_page import HomePage
from pages.products_page import ProductsPage


def load_test_data():
    project_root = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )

    file_path = os.path.join(
        project_root,
        "testdata",
        "search_data.json"
    )

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


@given("the user opens the Automation Exercise website")
def step_open_website(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

    context.home_page = HomePage(context.driver)
    context.products_page = ProductsPage(context.driver)

    context.home_page.open()

    context.test_data = load_test_data()

    print("Automation Exercise website opened")
    print("Search test data loaded")


@when("the user navigates to the products page")
def step_navigate_products(context):
    context.home_page.click_products()

    print("Products page opened")


@when('the user searches for "{product_name}"')
def step_search_product(context, product_name):
    context.search_product = product_name

    context.products_page.search_product(product_name)

    print(f"Searching for: {product_name}")


@then('the search results should contain "{product_name}"')
def step_verify_product(context, product_name):
    products = context.products_page.get_product_names()

    # Verify the requested product exists in external test data
    expected_products = [
        product["name"]
        for product in context.test_data["products"]
    ]

    assert product_name in expected_products

    # Verify the product actually appears in the website results
    assert any(
        product_name.lower() in product.lower()
        for product in products
    )

    print(f"Product found: {product_name}")


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()