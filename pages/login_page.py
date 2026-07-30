class LoginPage:
    def __init__(self, page):
        self.page = page
        self.login_page_content = page.locator('#main-content')
        self.agree_cookies_button = page.locator('#didomi-notice-agree-button')
        self.username_input = page.locator('aside #userName')
        self.password_input = page.locator('aside #password')
        # TODO: following selector should be updated
        self.login_button = page.locator('form button', has_text="Prihlásiť").locator("visible=true")
        # TODO: following selector should be updated, class may be changed in the future
        self.email_inbox_link = page.locator('a.MailBoxCentrum_mail__qEfcw')

    def agree_with_cookies(self):
        self.agree_cookies_button.click()
    
    def fill_credentials(self, email, password):
        self.username_input.fill(email)
        self.password_input.fill(password)
    
    def click_login(self):
        self.login_button.click()

    def click_email_link(self):
        self.email_inbox_link.click()
