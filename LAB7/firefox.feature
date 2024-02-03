Feature: Selenium Documentation Tests

  Scenario: Perform Various Tests on Selenium Documentation
    Given I open the Selenium documentation
    Then the test passes

    # Test 1: Maximize the window
    When I maximize the window
    Then the test passes

    # Test 2: Click on the link "1. Installation"
    When I click on the link firefox "1. Installation"
    Then the test passes

    # Test 3: Scroll down the page
    When I scroll down the page
    Then the test passes

    # Test 4: Scroll up the page
    When I scroll up the page
    Then the test passes

    # Test 5: Go back to the main page
    When I go back to the main page
    Then the test passes
