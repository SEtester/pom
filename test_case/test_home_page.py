# encoding:utf-8

import os
import sys

pom_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, pom_path)

from pages.home_page import HomePage
from common.driver import start_up_driver
import unittest
from time import sleep


class TestHomePageCase(unittest.TestCase):


    def setUp(self):
        self.driver = start_up_driver()

    def tearDown(self):
        self.driver.quit()

    def test_open_page_business_mailbox(self):
        home_page = HomePage(self.driver, '/')
        windows_handles = home_page.window_handles
        print(home_page.current_window_handle)

        business_mailbox_page = home_page.open_web_page_of_business_mailbox()
        self.assertTrue(business_mailbox_page.assert_new_window_is_opened(windows_handles))

        business_mailbox_page_handles = business_mailbox_page.window_handles[1]
        print(business_mailbox_page_handles)

        business_mailbox_page.switch_to_window(business_mailbox_page_handles)
        self.assertTrue('qiye' in business_mailbox_page.current_url)
        self.assertEqual('网易企业邮箱 - 企业邮箱信息化专业解决方案',business_mailbox_page.title)





if __name__ == '__main__':
    unittest.main()
