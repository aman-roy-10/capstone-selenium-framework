Feature: Product search

  Scenario: Search for a valid product
    Given the user opens the Automation Exercise website
    When the user navigates to the products page
    And the user searches for "Blue Top"
    Then the search results should contain "Blue Top"