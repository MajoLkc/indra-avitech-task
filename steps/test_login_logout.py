import os
from pytest_bdd import scenarios, given, when, then
from dotenv import load_dotenv
from playwright.sync_api import expect

load_dotenv()
scenarios("../features/login_logout.feature")


@given("user is on the email login page")
def go_to_login_page(page, login_page):
    page.goto("/")
    login_page.agree_with_cookies()


@when("user fills email and password fields with valid credentials")
def fill_credentials(login_page):
    login_page.fill_credentials(os.getenv("EMAIL"), os.getenv("PASSWORD"))


@when("user provides login")
def click_login(login_page):
    login_page.click_login()
    login_page.click_email_link()


@then("user's inbox page shall be displayed")
def check_inbox(mail_inbox_page):
    expect(mail_inbox_page.mails_panel).to_be_visible()
    

@when("user clicks on logout button")
def click_logout(mail_inbox_page):
    mail_inbox_page.click_logout()


@then("email login page shall be displayed")
def check_login_page(login_page):
    expect(login_page.login_page_content).to_be_visible()
