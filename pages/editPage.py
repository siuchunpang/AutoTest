from selenium.webdriver.common.by import By
from pages.basePage import Page
from pynput.mouse import Button, Controller
import time


class EditPage(Page):
    # 新增热点
    hot_menu = (By.XPATH, '/html/body/div[3]/div[1]/ul/li[4]')
    new_hot = (By.XPATH, '/html/body/div[3]/div[3]/div[1]/ul/li[1]/div/button')
    style = (By.XPATH, '/html/body/div[3]/div[3]/div[2]/div[2]/ul/li[1]/ul/li[6]')
    step_one = (By.XPATH, '/html/body/div[3]/div[2]/div[2]/div')
    step_two = (By.XPATH, '/html/body/div[3]/div[3]/div[2]/div[2]/ul/li[3]/div[2]/input')
    step_three = (By.XPATH, '/html/body/div[3]/div[3]/div[2]/div[2]/ul/li[3]/div[4]/div[1]/div[1]')
    step_four = (By.XPATH, '/html/body/div[3]/div[3]/div[2]/div[3]/button[1]')

    # 编辑场景信息
    old_title = (By.ID, 'pjtName')
    old_content = (By.XPATH, '//*[@id="edit2"]/div[1]')
    old_link_text = (By.XPATH, '/html/body/div[3]/div[3]/div[6]/ul/li[2]/div[4]/input[1]')
    old_link_address = (By.XPATH, '/html/body/div[3]/div[3]/div[6]/ul/li[2]/div[4]/input[2]')
    confirm_link_button = (By.XPATH, '/html/body/div[3]/div[3]/div[6]/ul/li[2]/div[5]/button[1]')
    save_and_publish_button = (By.ID, 'save')

    # 保存并发布后的提示
    tips_title = (By.XPATH, '/html/body/div[1]/div[4]/div/div[3]/div[1]')
    tips_content = (By.XPATH, '/html/body/div[1]/div[4]/div/div[3]/div[2]')

    # 初始化鼠标
    mouse = Controller()

    def is_tips_title(self):
        result = self.is_visible_element(self.tips_title)
        return result

    def is_tips_content(self):
        result = self.is_visible_element(self.tips_content)
        return result

    def drag_and_drop(self, x, y):
        self.mouse.press(Button.left)
        self.mouse.move(x, y)
        time.sleep(1)
        self.mouse.release(Button.left)
        # print('Now we have moved it to {0}'.format(self.mouse.position))

    def add_hot(self):
        # 热点菜单
        self.mouse.position = (880, 565)
        self.mouse.click(Button.right, 1)
        self.click(self.hot_menu)

        # 新增热点
        time.sleep(0.5)
        self.click(self.new_hot)

        # 选择热点样式
        time.sleep(0.5)
        self.click(self.style)

        # 编辑热点
        self.mouse.position = (880, 565)
        time.sleep(0.5)
        self.drag_and_drop(-100, -100)
        time.sleep(0.5)
        self.click(self.step_one)
        time.sleep(0.5)
        self.click(self.step_one)
        time.sleep(0.5)
        self.input_text(self.step_two, text='自动化热点')
        time.sleep(0.5)
        self.input_text(self.step_three, '自动化热点的简介')
        time.sleep(0.5)
        self.click(self.step_four)

    def edit_scene_info(self, keyword, new_info):
        if keyword == '标题':
            self.clear_text(self.old_title)
            time.sleep(0.5)
            self.input_text(self.old_title, new_info)
        elif keyword == '简介':
            self.clear_text(self.old_content)
            time.sleep(0.5)
            self.input_text(self.old_content, new_info)
        elif keyword == '链接文本':
            self.clear_text(self.old_link_text)
            time.sleep(0.5)
            self.input_text(self.old_link_text, new_info)
        elif keyword == '链接地址':
            self.clear_text(self.old_link_address)
            time.sleep(0.5)
            self.input_text(self.old_link_address, new_info)

    def confirm_link(self):
        self.click(self.confirm_link_button)

    def save_and_publish(self):
        self.click(self.save_and_publish_button)



