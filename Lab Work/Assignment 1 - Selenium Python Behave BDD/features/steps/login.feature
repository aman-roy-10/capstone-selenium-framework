Feature: Login functionality

  Scenario: Successful login with valid credentials
    Given the user opens the login application
    When the user enters valid username and password
    And the user clicks the login button
    Then the user should be logged in successfully