# encoding:utf8

import os
import sys

pom_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, pom_path)

from pages.home_page import HomePage
from common.driver import start_up_driver
import unittest
from time import sleep

class TestLoginCase(unittest.TestCase):

    def setUp(self):
        self.driver = start_up_driver()

    def tearDown(self):
        self.driver.quit()

    def test_send_email_success(self):
        username = 'xxxxxxxx'
        password = 'xxxxxxxx'
        home_page = HomePage(self.driver, '/')
        email_home_page = home_page.login(username, password)
        login_account_text = email_home_page.get_email_account_text()
        self.assertTrue(username in login_account_text)
        send_email_page = email_home_page.load_web_page_of_write_letter()
        send_email_page.enter_the_content_of_the_letter('test11111')
        sleep(5)


if __name__ == '__main__':
    unittest.main(verbosity=2)
