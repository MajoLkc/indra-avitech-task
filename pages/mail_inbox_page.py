class MailInboxPage:
    def __init__(self, page):
        self.page = page
        self.mails_panel = page.locator('#left_panel')
        self.logout_button = page.locator('#qa_logout_ju2')
    
    def click_logout(self):
        self.logout_button.click()

