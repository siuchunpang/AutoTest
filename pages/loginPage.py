from selenium.webdriver.common.by import By
from pages.basePage import Page
import time


class LoginPage(Page):
    # 用户登陆
    accoun_icon = (By.XPATH, '//*[@id="app"]/div[1]/div/div[3]/a[2]')
    user_name = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[2]/div/div[1]/div[1]/input')
    pass_word = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[2]/div/div[1]/div[2]/input')
    submit = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[2]/div/div[1]/div[4]/div[1]')
    cart_icon = (By.XPATH, '//*[@id="app"]/div[1]/div/div[3]/a[2]/div[2]')

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, usr, psw):
        self.click(self.accoun_icon)
        time.sleep(0.5)
        self.input_text(self.user_name, text=usr)
        time.sleep(0.5)
        self.input_text(self.pass_word, text=psw)
        time.sleep(0.5)
        self.click(self.submit)
        time.sleep(3)

    def is_login(self):
        result = self.is_visible_element(self.cart_icon)
        return result
