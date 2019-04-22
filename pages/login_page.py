# encoding:utf-8

from .base_page import BasePage
from .home_page import HomePage


class LoginPage(BasePage):

    @property
    def form_username(self):
        return self.by_css('#username')

    @property
    def form_password(self):
        return self.by_css('#password')

    @property
    def form_verification_code(self):
        return self.by_css('#verificationCode')

    @property
    def login_button(self):
        return self.by_css('#accountsLoginBtn')

    @property
    def error_msg(self):
        return self.by_css('.layui-layer-content', text=1)

    def login(self, username, password, code='xxxxxxxxxxxx'):
        self.form_username.send_keys(username)
        self.form_password.send_keys(password)
        self.form_verification_code.send_keys(code)
        self.login_button.click()
        return HomePage(self.driver)
