# encoding:utf-8


from .base_page import BasePage
from .mailbox_home_page import MailboxHomePage


class HomePage(BasePage):

    @property
    def email_login(self):
        return self.by_css('#lbNormal')

    @property
    def form_username(self):
        return self.by_css('.j-inputtext.dlemail.j-nameforslide')

    @property
    def form_password(self):
        return self.by_css('.j-inputtext.dlpwd')

    @property
    def login_button(self):
        return self.by_css('#dologin')

    @property
    def login_iframe(self):
        return self.by_css('.loginUrs iframe')

    def login(self, username, password):
        self.email_login.click()
        self.switch_to_frame(self.login_iframe)
        self.form_username.send_keys(username)
        self.form_password.send_keys(password)
        self.login_button.click()
        return MailboxHomePage(self.driver)
