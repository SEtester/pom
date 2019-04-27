# encoding:utf-8


from .base_page import BasePage

class MailboxHomePage(BasePage):

    @property
    def email_account(self):
        return self.by_css('#spnUid',text=1)

    def get_email_account_text(self):
        return self.email_account.text