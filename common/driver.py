#encoding:utf-8

from selenium import webdriver



def start_up_driver(browser_name='Chrome'):
    if browser_name == 'Chrome':
        driver = webdriver.Chrome()
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
            "Not found %s browser,You can enter 'Chrome', 'Firefox', 'Ie', 'Edge', 'Safari' ." % browser_name)
    return driver