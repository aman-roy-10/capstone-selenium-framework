import json
import os
import requests

from behave import given, when, then


BASE_URL = "https://jsonplaceholder.typicode.com"


def load_test_data():
    project_root = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )

    file_path = os.path.join(
        project_root,
        "testdata",
        "api_test_data.json"
    )

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


@given("the API service is available")
def step_api_service_available(context):
    response = requests.get(
        f"{BASE_URL}/users/1",
        timeout=10
    )

    assert response.status_code == 200

    context.test_data = load_test_data()

    print("API service is available")
    print("Test data loaded from JSON")


@when('I request user with id "{user_id}"')
def step_request_user(context, user_id):
    context.user_id = int(user_id)

    context.response = requests.get(
        f"{BASE_URL}/users/{user_id}",
        timeout=10
    )

    context.response_data = context.response.json()


@then("the API response status should be 200")
def step_verify_status(context):
    assert context.response.status_code == 200

    print(
        f"User ID {context.user_id}: "
        f"HTTP status {context.response.status_code}"
    )


@then('the response should contain name "{expected_name}"')
def step_verify_name(context, expected_name):
    actual_name = context.response_data["name"]

    json_user = next(
        user for user in context.test_data["users"]
        if user["id"] == context.user_id
    )

    assert json_user["name"] == expected_name
    assert actual_name == json_user["name"]

    print(f"Expected name: {expected_name}")
    print(f"Actual API name: {actual_name}")
    print("User data verified successfully")