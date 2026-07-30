import pytest
from pages.login_page import LoginPage
from pages.mail_inbox_page import MailInboxPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def mail_inbox_page(page):
    return MailInboxPage(page)