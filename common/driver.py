#encoding:utf-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def start_up_driver(browser_name='Chrome'):
    if browser_name == 'Chrome':
        driver = webdriver.Chrome()
    elif browser_name == "chrome_headless":
        options = Options()
        options.add_argument("--headless")  # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox')  # Bypass OS security model
        options.add_argument('--disable-gpu')  # applicable to windows os only
        driver = webdriver.Chrome(options=options)
    elif browser_name == 'Firefox':
        driver = webdriver.Firefox()
    elif browser_name == 'Ie':
        driver = webdriver.Ie()
    elif browser_name == 'Edge':
        driver = webdriver.Edge()
    elif browser_name == 'Safari':
        driver = webdriver.Safari()
    else:
        raise NameError(
            "Not found %s browser,You can enter 'Chrome', 'Firefox', 'Ie', 'Edge', 'Safari','chrome-headless'." % browser_name)
    return driver