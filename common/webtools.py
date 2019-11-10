from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


class webtools:
    def __init__(self, browser_type):
        self.browser_type = browser_type
        self.driver = None

    def open_browser(self):
        if self.browser_type == 'Chrome':
            self.driver = webdriver.Chrome()
        elif self.browser_type == 'Firefox':
            self.driver = webdriver.Firefox()
        elif self.browser_type == 'IE':
            self.driver = webdriver.Ie()
        self.driver.maximize_window()

    def is_element_visible(self, element):
        driver = self.open_browser
        try:
            the_element = EC.visibility_of_element_located(element)
            assert the_element(driver)
            flag = True
        except AssertionError as e:
            flag = False
            print(e)
        return flag
