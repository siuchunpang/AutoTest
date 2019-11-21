import unittest
import time
from pages.loginPage import LoginPage
from selenium import webdriver


# 四维看看登录测试
class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    # 输入正确的账号密码登录
    def test_login_right_testcase(self):
        # 创建Page对象
        login_page = LoginPage(self.driver)

        # 启动浏览器，进入四维看看首页
        login_page.get_webpage()

        # 登录
        login_page.login('13631262926', '1111111111')

        # 断言
        result = login_page.is_login()
        print("case1_is_login:" + str(result))
        self.assertTrue(result)

    # 输入错误的账号密码登录
    def test_login_wrongpsw_testcase(self):
        login_page = LoginPage(self.driver)
        login_page.get_webpage()
        login_page.login('13631262926', '12345678')
        time.sleep(1)
        # 截图错误提示
        login_page.save_img(self.test_login_wrongpsw_testcase.__name__, 'login_wrongpsw.img')
        result = login_page.is_login()
        print("case2_is_login:" + str(result))
        self.assertFalse(result)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
