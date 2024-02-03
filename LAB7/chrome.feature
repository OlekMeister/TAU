Feature: The Internet Application Tests

  Scenario: Perform Various Tests on the Internet Application
    Given I open the application

    # Test 1: Click on A/B Testing link
    When I click on the link chrome "A/B Testing"
    Then the test passes

    # Test 2: Go back to the main page and add an element
    When I go back to the main page and click on the link "Add/Remove Elements"
    And I click the "Add Element" button
    Then the element is added successfully
    And the test passes

    # Test 3: Remove the added element
    When I go back to the main page and click on the link "Add/Remove Elements"
    And I click the "Add Element" button
    And I remove the added element
    Then the element is removed successfully
    And the test passes

    # Test 4: Check the checkbox
    When I go back to the main page and click on the link "Checkboxes"
    And I check the checkbox
    Then the checkbox is checked successfully
    And the test passes
