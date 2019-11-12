import time
from selenium.webdriver.support import expected_conditions as EC


class Page(object):
    def __init__(self, driver, base_url="https://pro.4dkankan.com"):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30

    def get_webpage(self):
        self.driver.get(self.base_url)

    def goto_scene_edit_page(self, scene_url):
        self.driver.get(self.base_url + scene_url)
        time.sleep(10)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def input_text(self, loc, text):
        self.find_element(*loc).send_keys(text)

    def clear_text(self, loc):
        self.find_element(*loc).clear()

    def click(self, loc):
        self.find_element(*loc).click()

    def get_title(self):
        return self.driver.find_element_by_xpath('/html/head/title').text

    def is_element_visible(self, element):
        driver = self.driver
        try:
            the_element = EC.visibility_of_element_located(element)
            assert the_element(driver)
            flag = True
        except AssertionError as e:
            flag = False
            print(e)
        return flag

