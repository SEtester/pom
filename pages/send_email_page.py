# encoding:utf-8


from .base_page import BasePage
from time import sleep


class SendEmailPage(BasePage):

    def just_text(self):
        print('test_send_email_page')
        sleep(5)

    @property
    def email_context_iframe(self):
        return self.by_css('.APP-editor-iframe')

    @property
    def email_context(self):
        return self.by_css('body.nui-scroll')

    def enter_the_content_of_the_letter(self,context):
        self.switch_to_frame(self.email_context_iframe)
        # self.email_context.click()
        self.email_context.send_keys(context)

