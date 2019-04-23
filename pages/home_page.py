# encoding:utf-8


from .base_page import BasePage


class HomePage(BasePage):

    @property
    def username(self):
        return self.by_css('.username a:nth-child(1)', text=1)

    def username_text(self):
        return self.username.text

