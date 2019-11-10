from selenium.webdriver.common.by import By
from pages.basePage import Page
import time


class LoginPage(Page):
    # 用户登陆
    accountIcon = (By.XPATH, '//*[@id="app"]/div[1]/div/div[3]/a[2]')
    user_name = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[2]/div/div[1]/div[1]/input')
    pass_word = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[2]/div/div[1]/div[2]/input')
    submit = (By.XPATH, '//*[@id="app"]/div[3]/div[2]/div[2]/div/div[1]/div[4]/div[1]')

    def __init__(self, usr, psw):
        self.usr = usr
        self.psw = psw

    def login(self):
        self.click(self.accountIcon)
        time.sleep(0.5)
        self.input_text(self.user_name, text=self.usr)
        time.sleep(0.5)
        self.input_text(self.pass_word, text=self.psw)
        time.sleep(0.5)
        self.click(self.submit)
