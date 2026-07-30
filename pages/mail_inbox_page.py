from playwright.sync_api import TimeoutError


class MailInboxPage:
    def __init__(self, page):
        self.page = page
        self.mails_panel = page.locator('#left_panel')
        self.logout_button = page.locator('#qa_logout_ju2')
        self.write_mail_button = self.mails_panel.locator('#compose_button')
        self.mail_form = page.locator("#mail_composer_frm")
        self.send_button = self.mail_form.locator("#qa_email_send_upper")
        self.contacts_button = self.mail_form.locator("#qabook_switch_names")
        self.contacts_list = self.mail_form.locator("#quickabook_div")
        # following locator is not unique, it matches all contacts in the list
        self.contact = self.contacts_list.locator("span")
        self.recipient_input = self.mail_form.locator("#recipient_rightclick_to")
        self.subject_input = self.mail_form.locator("#subject_input")
        self.attachment_input = self.mail_form.locator("#mc_attachments_add")
        self.mail_text_input = page.frame_locator('#mail_composer_body_ifr').locator("#tinymce")
        self.sent_mails_label = page.locator("#fld_1_line")
        self.mails_list = page.locator("#mail_list_frm")
        # following 3 locators are not unique, they match all mails
        self.mail = self.mails_list.locator(".list-row") 
        self.subject = self.mail.locator(".list-object") 
        self.recipient = self.mail.locator(".list-sender")

    def click_logout(self):
        self.logout_button.click()

    def click_create_message(self):
        self.write_mail_button.click()

    def select_recipient(self, recipient_name, recipient_email):
        self.contacts_button.click()
        contact = self.contact.filter(has_text=recipient_name)
        try:
            contact.wait_for(state="visible", timeout=5000)
            contact.click()
        except TimeoutError:
            self.recipient_input.fill(recipient_email)

    def fill_subject(self, text):
        self.subject_input.fill(text)

    def fill_email_text(self, text):
        self.mail_text_input.fill(text)

    def add_attachment(self, file_path):
        self.attachment_input.set_input_files(file_path)

    def click_send(self):
        self.send_button.click()

    def navigate_to_sent_mails(self):
        self.sent_mails_label.click()
