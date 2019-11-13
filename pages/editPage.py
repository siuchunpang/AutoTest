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
    info = (By.XPATH, '//*[@id="text-elem760714163310138"]/p')

    # 初始化鼠标
    mouse = Controller()

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

    def edit_scene_info(self):
        self.clear_text(self.old_title)
        time.sleep(0.5)
        new_title = '测试是否断连'
        self.input_text(self.old_title, new_title)


