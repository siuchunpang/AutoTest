from selenium.webdriver.common.by import By
from pages.basePage import Page
import time


class EditBasicSettingPage(Page):
    # 二维码
    download_QRCode = (By.ID, 'QRcodeDownload')
    upload_QRCode = (By.ID, 'QRupload')

    # 场景地址
    copy_link = (By.XPATH, '//*[@id="copyLink"]/div/label')
    link = (By.XPATH, '//*[@id="copyLink"]/a')

    # 背景音乐
    music = (By.XPATH, '/html/body/div[3]/div[3]/div[5]/ul/li[3]/div[2]/a')
    music_list = (By.XPATH, '/html/body/div[3]/div[3]/div[5]/ul/li[3]/div[2]/ul/li[4]')

    # 基础设置
    pano_visi = (By.XPATH, '/html/body/div[3]/div[3]/div[5]/ul/li[4]/div[1]/div')
    m2d_visi = (By.XPATH, '/html/body/div[3]/div[3]/div[5]/ul/li[4]/div[2]/div')
    m3d_visi = (By.XPATH, '/html/body/div[3]/div[3]/div[5]/ul/li[4]/div[3]/div')
    map_visi = (By.XPATH, '/html/body/div[3]/div[3]/div[5]/ul/li[4]/div[4]/div')
    vr_visi = (By.XPATH, '/html/body/div[3]/div[3]/div[5]/ul/li[4]/div[5]/div')
    tour_visi = (By.XPATH, '/html/body/div[3]/div[3]/div[5]/ul/li[4]/div[6]/div')
    ruler_visi = (By.XPATH, '/html/body/div[3]/div[3]/div[5]/ul/li[4]/div[7]/div')
    cad_img_visi = (By.XPATH, '/html/body/div[3]/div[3]/div[5]/ul/li[4]/div[8]/div')
    measure_visi = (By.XPATH, '/html/body/div[3]/div[3]/div[5]/ul/li[4]/div[9]/div')




