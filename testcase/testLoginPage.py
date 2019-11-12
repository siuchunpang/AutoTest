import unittest
import time
from pages.loginPage import LoginPage
from selenium import webdriver


# 四维看看测试
class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    # 输入正确的账号密码登录
    def test_right_login(self):
        # 创建Page对象
        login_page = LoginPage(self.driver)

        # 启动浏览器，进入四维看看首页
        login_page.get_webpage()

        # 登录
        login_page.login('13631262926', 'junpeng123')

        # 断言
        login_page.is_login()

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()


