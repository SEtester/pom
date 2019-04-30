# encoding:utf-8


from .base_page import BasePage


class BsMailboxPage(BasePage):

    def switch_to_home_page(self):
        self.close()
        self.switch_to_window(self.window_handles[0])
