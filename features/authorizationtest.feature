# Created by user at 16.03.2023
Feature: Testing authorization

  Scenario: User go to website and use its creds for authorization
    Given I am navigate to website
    When Click Log in button
    When Enter my creds
    And Click Authorization button
    Then I successfully authorized on website
