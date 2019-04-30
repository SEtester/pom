# encoding:utf-8


from .base_page import BasePage
from .emailbox_home_page import MailboxHomePage
from .business_mailbox_page import BsMailboxPage


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

    @property
    def business_mailbox(self):
        return self.by_css('.headerNav a:nth-child(1)')

    # def open_web_page_of_business_mailbox(self):
    #     self.business_mailbox.click()
    #     return BsMailboxPage(self.driver)

    def open_web_page_of_business_mailbox(self):
        home_page_current_handle = self.window_handles
        self.business_mailbox.click()
        assert self.assert_new_window_is_opened(home_page_current_handle)
        window_handles = self.window_handles
        self.switch_to_window(window_handles[1])
        return BsMailboxPage(self.driver)

    def login(self, username, password):
        self.email_login.click()
        self.switch_to_frame(self.login_iframe)
        self.form_username.send_keys(username)
        self.form_password.send_keys(password)
        self.login_button.click()
        return MailboxHomePage(self.driver)
