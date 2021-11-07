Feature:  URL login

  Scenario: check the URL and login
    Given launch chrome browser
    When user get the URL
    Then check the logo
    And close
