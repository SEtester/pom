# encoding:utf-8


from .base_page import BasePage
from .send_email_page import SendEmailPage


class MailboxHomePage(BasePage):

    @property
    def email_account(self):
        return self.by_css('#spnUid', text=1)

    @property
    def write_a_letter(self):
        return self.by_css('#_mail_component_24_24 .oz0')

    def load_web_page_of_write_letter(self):
        self.write_a_letter.click()
        return SendEmailPage(self.driver)

    def get_email_account_text(self):
        return self.email_account.text

