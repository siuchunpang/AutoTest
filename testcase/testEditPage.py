import unittest
import time
from selenium import webdriver
from pages.editPage import EditPage
from pages.loginPage import LoginPage
from pages.basePage import Page
from BeautifulReport import BeautifulReport as br


# 四维看看测试
class TestEditPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # 场景网址
        scene_url = '/editProPC.html?m=opT87AQtZ'
        # 期望验证的场景标题
        assert_title = '测试是否断连'
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

        # 验证标题
        self.assertEqual(page.get_scene_title(), assert_title, msg='场景标题不正确')

    @br.add_test_img('测试场景信息.png')
    def testSceneInfo(self):
        driver = self.driver
        edit_page = EditPage(driver)

        # 编辑场景信息
        print('编辑场景信息')
        edit_page.edit_scene_info()
        print('场景信息修改成功')

    '''
    @br.add_test_img('测试热点.png')
    def testHot(self):
        driver = self.driver
        edit_page = EditPage(driver)

        # 添加热点
        print('添加热点')
        edit_page.add_hot()
        print('成功添加热点')
    '''

    def tearDown(self):
        self.driver.quit()
