Feature: Login and logout to my email address

    Scenario: User logs in and logs out of his email account
        Given user is on the email login page
        When user fills email and password fields with valid credentials
        And user clicks on login button
        Then user's inbox page shall be displayed
        When user clicks on logout button
        Then email login page shall be displayed 