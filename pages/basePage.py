import time


class Page(object):
    def __init__(self, driver, base_url="https://pro.4dkankan.com"):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30

    def goto_homePage(self):
        self.driver.get(self.base_url)

    def goto_sceneEdit(self, scene_url):
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

    # def get_title(self):
    #     return self.driver.find_element_by_xpath('/html/body/div[2]/span').text


