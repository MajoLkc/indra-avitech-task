Feature: Send email

    Background: Provide login
        Given user is on the email login page
        When user fills email and password fields with valid credentials
        And user provides login
        Then user's inbox page shall be displayed

    Scenario: User sends email with attachment to the email address from contacts
        When user clicks on create message button
        Then new email component shall be displayed
        When user selects recipient from contacts
        And user adds subject and email text
        And user adds attachment
        And user clicks on send button
        Then email with attachment shall be sent
        When user clicks on logout button
        Then email login page shall be displayed 