#encoding:utf-8
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException

# from selenium.webdriver.support.expected_conditions import *

"""
 * Canned "Expected Conditions" which are generally useful within webdriver
 * tests.
"""



class text_not_to_be_empty_in_element(object):
    """ An expectation for checking if the given text is present in the
    specified element.
    locator, text
    """
    def __init__(self, locator, text_=''):
        self.locator = locator
        self.text = text_

    def __call__(self, driver):
        try:
            element_text = _find_element(driver, self.locator).text
            return self.text != element_text
        except StaleElementReferenceException:
            return False

def _find_element(driver, by):
    """Looks up an element. Logs and re-raises ``WebDriverException``
    if thrown."""
    try:
        return driver.find_element(*by)
    except NoSuchElementException as e:
        raise e
    except WebDriverException as e:
        raise e
