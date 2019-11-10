import unittest
import time
from common import webtools
from pages.loginPage import LoginPage


# 四维看看测试
class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webtools.common_driver()

    # 输入正确的账号密码登录
    def testLogin(self):
        driver = self.driver
        # 四维看看测试首页
        base_url = "http://pro.4dkankan.com"

        # 创建Page对象
        login_Page = LoginPage('13631262926', 'junpeng123')

        # 启动浏览器，进入四维看看首页
        login_Page.goto_homePage()
        driver.maximize_window()

        # 登录
        login_Page.login()

        # 断言


    def tearDown(self):
        time.sleep(10)
        self.driver.quit()


