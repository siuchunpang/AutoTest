import unittest
import time
from selenium import webdriver
from pages.editBasicSettingPage import EditBasicSettingPage
from pages.loginPage import LoginPage
from pages.basePage import Page
from BeautifulReport import BeautifulReport as br


# 四维看看测试
class TestEditBasicSettingPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # 场景网址
        scene_url = '/editProPC.html?m=opT87AQtZ'
        # 期望验证的场景标题
        assert_title = '自动化测试'
        print('场景标题：' + assert_title)

        # 创建Page对象
        page = Page(self.driver)
        login_page = LoginPage(self.driver)

        # 启动浏览器，进入四维看看首页
        page.get_webpage()
        self.driver.maximize_window()

        # 登录
        login_page.login('13631262926', '1111111111')

        # 进入场景编辑界面
        page.goto_scene_edit_page(scene_url)

    # 修改场景信息，保存并发布
    @br.add_test_img('测试基础设置.png')
    def testQRCode(self):
        pass

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
