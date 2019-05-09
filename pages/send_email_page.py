# encoding:utf-8


from .base_page import BasePage


class SendEmailPage(BasePage):

    @property
    def email_context_iframe(self):
        return self.by_css('.APP-editor-iframe')

    @property
    def email_context(self):
        return self.by_css('body.nui-scroll')

    @property
    def recipient(self):
        return self.by_css('.nui-editableAddr-ipt')
        # return self.by_xpath('//div[@class="bz0"]/div[2]//input')

    @property
    def email_subject(self):
        return self.by_css('.bz0 .nui-ipt-input')

    @property
    def send_email_button(self):
        return self.by_css('.js-component-button.nui-mainBtn.nui-btn.nui-btn-hasIcon.nui-mainBtn-hasIcon')

    @property
    def send_email_success(self):
        return self.by_css('.tK1')

    def get_send_email_success_text(self):
        return self.send_email_success.text

    def set_content(self, content):
        js = "document.querySelector('.APP-editor-iframe').contentWindow.document.body.innerHTML = '%s'" % (content)
        self.execute_script(js)

    def enter_the_content_of_the_letter(self, recipient, email_subject, context):
        self.recipient.send_keys(recipient)
        self.email_subject.send_keys(email_subject)
        # self.switch_to_frame(self.email_context_iframe)
        # self.email_context.send_keys(context)
        # self.set_content(context)
        self.send_email_button.click()
        self.switch_to_default_content()