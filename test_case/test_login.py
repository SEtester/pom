# encoding:utf-8

import os
import sys

pom_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(pom_path)
sys.path.insert(0, pom_path)

from selenium import webdriver
from pages.login_page import LoginPage
import unittest


class TestLoginCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_login_success(self):
        username = 'xxxxxx'
        password = 'xxxxxx'
        login_page = LoginPage(self.driver, path='/view/login.shtml')
        home_page = login_page.login(username, password)
        username_ = home_page.username_text()
        self.assertEqual('xxxxxx', username_)
        self.assertTrue('/index' in home_page.current_url)


if __name__ == '__main__':
    unittest.main(verbosity=2)
