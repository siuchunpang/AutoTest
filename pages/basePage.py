import time


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
        element = self.driver.find_element(*loc)
        return element

    def input_text(self, loc, text):
        self.find_element(*loc).send_keys(text)

    def clear_text(self, loc):
        self.find_element(*loc).clear()

    def click(self, loc):
        self.find_element(*loc).click()

    def get_scene_title(self):
        title = self.driver.find_element_by_id('j-header-scenename').text
        return title

