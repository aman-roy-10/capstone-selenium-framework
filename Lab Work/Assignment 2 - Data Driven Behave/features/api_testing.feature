Feature: Data driven API testing

  Scenario Outline: Verify user API response
    Given the API service is available
    When I request user with id "<user_id>"
    Then the API response status should be 200
    And the response should contain name "<expected_name>"

    Examples:
      | user_id | expected_name    |
      | 1       | Leanne Graham    |
      | 2       | Ervin Howell     |
      | 3       | Clementine Bauch |