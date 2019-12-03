from selenium.webdriver.common.by import By
from pages.basePage import Page
import time


class EditSceneInfoPage(Page):
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

    def is_tips_title(self):
        result = self.is_visible_element(self.tips_title)
        return result

    def is_tips_content(self):
        result = self.is_visible_element(self.tips_content)
        return result

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



