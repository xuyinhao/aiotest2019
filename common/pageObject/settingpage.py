from selenium import webdriver
from common.base_page import BasePage
from common.logpy import LogHandler
from common.pageObject.homepageobj import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import time,sys
from conf import readconfig

class SettingPage(HomePage):
    global logg
    logg = LogHandler().getlog()
    base_setting_menu = (By.XPATH,"//div[@id='settingLeft']/div[1]")
    store_setting_menu = (By.XPATH,"//div[@id='settingLeft']/div[2]")
    cloud_setting_menu = (By.XPATH,"//div[@id='settingLeft']/div[3]")
    cltport_setting_menu = (By.XPATH,"//div[contains(text(),'客户端端口设置')]")
    cltport_num = (By.CSS_SELECTOR,"input.setting-input")
    cltport_save_btn = (By.NAME,"set-port")
    layout_setting_menu = (By.XPATH,"//div[contains(text(),'文件分布')]")
    getalarm_setting_menu = (By.XPATH,"//div[contains(text(),'告警订阅')]")
    netcardwarn_setting_menu = (By.XPATH,"//div[contains(text(),'网卡报警管理')]")
    license_setting_menu = (By.XPATH,"//div[contains(text(),'授权管理')]")
    #基础设置
    user_info_setting_menu = (By.XPATH,"//div[contains(text(),'用户信息')]")
    email_setting_menu = (By.XPATH,"//div[contains(text(),'邮件服务器设置')]")


    # def __init__(self):
    #     self.init_home_page()
    #     self.click_setting_menu()
    #     logg.info("click setting menu")

    def init_setting(self):
        #登录+点击设置
        self.init_home_page()
        self.click_setting_menu()
        logg.info("init and click setting menu")
        pass
    def click_base_setting(self):
        #点击设置
        self.click_btn(*self.base_setting_menu)
        logg.info("click  setting menu ")
        pass

    def click_store_setting(self):
        #存储管理设置
        self.click_btn(*self.store_setting_menu)
        logg.info("click store setting menu ")
        pass
    def click_layout_setting(self):
        self.click_btn(*self.layout_setting_menu)
        logg.info("clicj layout setting menu")
        pass
    def set_cltport(self,portnum):
        logg.info("set client  port:" + portnum)
        self.click_btn(*self.cltport_setting_menu)
        self.clear_text(*self.cltport_num)
        self.type_text(self.cltport_num,portnum)
        self.click_btn(*self.cltport_save_btn)
        sleep(1)
        if self.check_dialog_success("设置端口"):
            return True
        else:
            return  False

    def click_cloud_setting(self):
        self.click_btn(*self.cloud_setting_menu)
        logg.info("click cloud setting menu ")
        pass

if __name__ == '__main__':
    setpage = SettingPage(webdriver.Chrome())
    setpage.init_setting()
    setpage.click_store_setting()
    sleep(2)
    setpage.set_cltport("1234")

    # setpage.brower_quit_all()