# encoding:utf-8

import os
import sys

pom_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, pom_path)

from pages.home_page import HomePage
from common.driver import start_up_driver
import unittest


class TestLoginCase(unittest.TestCase):

    def setUp(self):
        self.driver = start_up_driver()

    def tearDown(self):
        self.driver.quit()

    def test_login_success(self):
        username = 'aa460060639'
        password = 'qwe2752773@ee'
        home_page = HomePage(self.driver, '/')
        email_home_page = home_page.login(username, password)
        login_account_text = email_home_page.get_email_account_text()
        self.assertTrue(username in login_account_text)


if __name__ == '__main__':
    unittest.main(verbosity=2)
