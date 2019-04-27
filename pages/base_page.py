# encoding:utf-8

import os
import sys

pom_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(pom_path)
sys.path.insert(0, pom_path)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from time import sleep
from pages import ec

# URL = 'https://tianhangbox.com'
URL = 'https://mail.163.com/'
TIME_OUT = 10
POLL_FREQUENCY = 0.5


class BasePage():

    def __init__(self, driver, path=None):
        """
        BasePage instance.

        :param driver: WebDriver instance
        :param path: uri
        :return: None
        """
        self.driver = driver
        # self.driver = webdriver.Chrome()
        self.load_web(path)

    # 导航到网页
    def load_web(self, path=None):
        if path != None:
            url = URL + path
            print('url:', url)
        else:
            url = None
        if path != None:
            self.driver.get(url)

    def by_css(self, css, text=None):
        locator = (By.CSS_SELECTOR, css)
        try:
            WebDriverWait(self.driver, timeout=TIME_OUT, poll_frequency=POLL_FREQUENCY).until(
                EC.visibility_of_element_located(locator))
            # 如果后台没有及时返回提示文案，则继续等待
            if text != None:
                WebDriverWait(self.driver, timeout=TIME_OUT, poll_frequency=POLL_FREQUENCY).until(
                    ec.text_not_to_be_empty_in_element(locator))
        except TimeoutException as e:
            msg = "Time out when locate element using %s: %s" % (locator[0], locator[-1])
            raise TimeoutException(msg)

        return self.driver.find_element(*locator)

    def by_xpath(self, xpath, text=None):
        locator = (By.XPATH, xpath)
        try:
            WebDriverWait(self.driver, timeout=TIME_OUT, poll_frequency=POLL_FREQUENCY).until(
                EC.visibility_of_element_located(locator))
            # 如果后台没有及时返回提示文案，则继续等待
            if text != None:
                WebDriverWait(self.driver, timeout=TIME_OUT, poll_frequency=POLL_FREQUENCY).until(
                    ec.text_not_to_be_empty_in_element(locator))
        except TimeoutException as e:
            msg = "Time out when locate element using %s: %s" % (locator[0], locator[-1])
            raise TimeoutException(msg)

        return self.driver.find_element(*locator)

    def switch_to_frame(self, frame_reference):
        """
         Switches focus to the specified frame, by index, name, or webelement.

         :Args:
          - frame_reference: The name of the window to switch to, an integer representing the index,
                             or a webelement that is an (i)frame to switch to.
        """
        return self.driver.switch_to.frame(frame_reference)

    def switch_to_default_content(self):
        """
        Switch focus to the default frame.
        """
        return self.driver.switch_to.default_content()

    def switch_to_parent_frame(self):
        """
        Switches focus to the parent context. If the current context is the top
        level browsing context, the context remains unchanged.
        """
        return self.driver.switch_to.parent_frame()

    @property
    def current_url(self):
        '''
        Gets the URL of the current page
        '''
        return self.driver.current_url

    @property
    def title(self):
        '''
        Returns the title of the current page.
        '''
        return self.driver.title

    @property
    def name(self):
        '''
        Returns the name of the underlying browser for this instance.
        '''
        return self.driver.name

    @property
    def current_window_handle(self):
        """
        Returns the handle of the current window.
        """
        return self.driver.current_window_handle

    @property
    def window_handles(self):
        """
        Returns the handles of all windows within the current session.
        """
        return self.driver.window_handles

    def switch_to_window(self, window_name):
        return self.driver.switch_to.window(window_name)

    def assert_new_window_is_opened(self, current_handles):
        return EC.new_window_is_opened(current_handles)(self.driver)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    base_page = BasePage(driver, path='/')
    # base_page = BasePage()
    base_page.by_css('#lbNormal').click()
    el = base_page.by_css('#loginDiv iframe')
    base_page.switch_to_frame(el)
    base_page.by_css('.j-inputtext.dlemail.j-nameforslide').send_keys('xxxxxx')
    # base_page.by_css('#password').send_keys('xxxxxx')
    # base_page.by_css('#verificationCode').send_keys('xxxxxx')
    # base_page.by_css('#accountsLoginBtn').click()
    # print(base_page.by_css('.layui-layer-content', text=1).text)
    sleep(3)
    print(base_page.current_window_handle)
    print(base_page.window_handles)
    # print(base_page.by_css('.layui-layer-content').text)
    # print(base_page.title)
    driver.quit()
