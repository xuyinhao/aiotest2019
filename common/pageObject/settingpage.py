from selenium import webdriver
from common.base_page import BasePage
from common.logpy import LogHandler
from common.pageObject.homepageobj import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import time, sys
from conf import readconfig
from common.global_element import GlobalElements


class SettingPage(HomePage):
    global logg
    logg = LogHandler().getlog()
    # 系统设置，设置菜单：基础设置、存储管理设置、虚拟云设置
    e_setting = GlobalElements.setting

    def init_setting(self):
        # 登录+点击设置
        self.init_home_page()
        self.click_setting_menu()
        logg.info("init and click setting menu")
        pass

    def click_base_setting(self):
        # 点击设置
        self.click_btn(*self.e_setting.base_setting_menu)
        logg.info("click  setting menu ")
        pass

    def click_store_setting(self):
        # 存储管理设置
        self.click_btn(*self.e_setting.store_setting_menu)
        logg.info("click store setting menu ")
        pass

    def click_layout_setting(self):
        self.click_btn(*self.e_setting.layout_setting_menu)
        logg.info("clicj layout setting menu")
        pass

    def set_cltport(self, portnum):
        logg.info("set client  port:" + portnum)
        self.click_btn(*self.e_setting.cltport_setting_menu)
        self.clear_text(*self.e_setting.cltport_num)
        self.type_text(self.e_setting.cltport_num, portnum)
        self.click_btn(*self.e_setting.cltport_save_btn)
        sleep(1)
        if self.check_dialog_success("设置端口"):
            return True
        else:
            return False

    def click_cloud_setting(self):
        self.click_btn(*self.e_setting.cloud_setting_menu)
        logg.info("click cloud setting menu ")
        pass


if __name__ == '__main__':
    setpage = SettingPage(webdriver.Chrome())
    setpage.init_setting()
    setpage.click_store_setting()
    sleep(2)
    setpage.set_cltport("40001")

    # setpage.brower_quit_all()
