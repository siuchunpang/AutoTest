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
        # 四维看看测试首页
        base_url = "http://test.4dkankan.com"

        # 场景网址
        scene_url = '/editPC.html?m=YTvZzX0b'
        # 期望验证的场景标题
        assert_title = '北京05311'
        print(assert_title)

        # 创建Page对象
        page = Page(self.driver, base_url)
        login_page = LoginPage(self.driver)

        # 启动浏览器，进入四维看看首页
        page.gotoHomePage()
        self.driver.maximize_window()

        # 登录
        login_page.login()

        # 进入场景编辑界面
        page.gotoSceneEdit(scene_url)

        # 验证标题
        self.assertEqual(page.get_title(), assert_title, msg='场景标题不正确')

    '''
    @br.add_test_img('测试场景信息.png')
    def testSceneInfo(self):
        driver = self.driver
        edit_page = EditPage(driver)

        # 编辑场景信息
        print('编辑场景信息')
        edit_page.edit_scene_info()
        print('修改成功')
    '''

    @br.add_test_img('测试热点.png')
    def testHot(self):
        driver = self.driver
        edit_page = EditPage(driver)

        # 添加热点
        print('添加热点')
        edit_page.add_hot()
        print('成功添加热点')

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()


