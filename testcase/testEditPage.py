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

        # 验证标题
        self.assertEqual(page.get_scene_title(), assert_title, msg='场景标题不正确')

    # 修改场景信息，保存并发布
    @br.add_test_img('测试场景信息.png')
    def testSceneInfo(self):
        title = "自动化测试"
        content = "四维看看 让空间讲故事 自动化测试\n"
        link_text = "自动化测试展示页面"
        link_address = "https://www.4dkankan.com/editProPC.html?m=opT87AQtZ"

        driver = self.driver
        edit_page = EditPage(driver)

        # 编辑场景信息
        edit_page.edit_scene_info("标题", title)
        print('修改后标题：' + title)
        edit_page.edit_scene_info("简介", content)
        print('修改后简介：' + content)
        edit_page.edit_scene_info("链接文本", link_text)
        print('修改后链接文本：' + link_text)
        edit_page.edit_scene_info("链接地址", link_address)
        edit_page.confirm_link()
        print('修改后链接地址：' + link_address)
        edit_page.save_and_publish()

        # 断言保存并发布的提示
        result_of_tips_title = edit_page.is_tips_title()
        print("result_of_tips_title:" + str(result_of_tips_title))
        self.assertTrue(result_of_tips_title)
        result_of_tips_content = edit_page.is_tips_content()
        print("result_of_tips_content:" + str(result_of_tips_content))
        self.assertTrue(result_of_tips_content)

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


if __name__ == "__main__":
    unittest.main()
