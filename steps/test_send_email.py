import os
from pytest_bdd import scenarios, given, when, then
from dotenv import load_dotenv
from playwright.sync_api import expect
from pathlib import Path

load_dotenv()
scenarios("../features/send_email.feature")


RECIPIENT = "Marián Lukáč"
RECIPIENT_EMAIL = "majo_lukac_test@centrum.sk"
SUBJECT_TEXT = "Subject"
MAIL_TEXT = "This is a test email message."
ATTACHMENT_PATH =  Path(__file__).parent.parent / "test_data" / "test_attachment.txt"

string_attachment_path = str(ATTACHMENT_PATH)


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


@when("user clicks on create message button")
def click_create_message(mail_inbox_page):
    mail_inbox_page.click_create_message()


@then("new email component shall be displayed")
def check_new_mail(mail_inbox_page):
    expect(mail_inbox_page.mail_form).to_be_visible()


@when("user selects recipient from contacts")
def select_recipient(mail_inbox_page):
    mail_inbox_page.select_recipient(RECIPIENT, RECIPIENT_EMAIL)


@when("user adds subject and email text")
def add_subject_and_text(mail_inbox_page):
    mail_inbox_page.fill_subject(SUBJECT_TEXT)
    mail_inbox_page.fill_email_text(MAIL_TEXT)


@when("user adds attachment")
def add_attachment(mail_inbox_page):
    mail_inbox_page.add_attachment(string_attachment_path)


@when("user clicks on send button")
def add_attachment(mail_inbox_page):
    mail_inbox_page.click_send()


@then("email with attachment shall be sent")
def check_sent_mails(mail_inbox_page):
    mail_inbox_page.navigate_to_sent_mails()
    expect(mail_inbox_page.subject.first).to_contain_text(SUBJECT_TEXT)
    expect(mail_inbox_page.recipient.first).to_have_text(RECIPIENT)


@when("user clicks on logout button")
def click_logout(mail_inbox_page):
    mail_inbox_page.click_logout()


@then("email login page shall be displayed")
def check_login_page(login_page):
    expect(login_page.login_page_content).to_be_visible()
