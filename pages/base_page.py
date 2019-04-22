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
from time import sleep
from pages import ec

URL = 'https://tianhangbox.com'
TIME_OUT = 20
POLL_FREQUENCY = 0.5


class BasePage():

    # 传入Webdriver实例 ， uri
    def __init__(self, driver, path=None):
        """
        BasePage instance.

        :param driver: WebDriver instance
        :param path: uri
        :return: None
        """
        # self.driver = webdriver.Chrome()
        self.driver = driver
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
        WebDriverWait(self.driver, timeout=TIME_OUT, poll_frequency=POLL_FREQUENCY).until(
            EC.visibility_of_element_located(locator))
        # 如果后台没有及时返回提示文案，则继续等待
        if text != None:
            WebDriverWait(self.driver, timeout=TIME_OUT, poll_frequency=POLL_FREQUENCY).until(
                ec.text_not_to_be_empty_in_element(locator))
            # WebDriverWait(self.driver, timeout=TIME_OUT, poll_frequency=POLL_FREQUENCY).until(
            #     EC.text_to_be_present_in_element(locator, text))
        return self.driver.find_element(*locator)

    def by_xpath(self, xpath, text=None):
        locator = (By.XPATH, xpath)
        WebDriverWait(self.driver, timeout=TIME_OUT, poll_frequency=POLL_FREQUENCY).until(
            EC.visibility_of_element_located(locator))
        # 如果后台没有及时返回提示文案，则继续等待
        if text != None:
            WebDriverWait(self.driver, timeout=TIME_OUT, poll_frequency=POLL_FREQUENCY).until(
                ec.text_not_to_be_empty_in_element(locator, text))
        return self.driver.find_element(*locator)

    @property
    def current_url(self):
        return self.driver.current_url


if __name__ == '__main__':
    driver = webdriver.Chrome()
    base_page = BasePage(driver, path='/view/login.shtml')
    # base_page = BasePage()
    base_page.by_css('#username').send_keys('xxxxxx')
    base_page.by_css('#password').send_keys('xxxxxx')
    base_page.by_css('#verificationCode').send_keys('xxxxxx')
    base_page.by_css('#accountsLoginBtn').click()
    print(base_page.by_css('.layui-layer-content', text=1).text)
    sleep(3)
    print(base_page.by_css('.layui-layer-content').text)
