from selenium import webdriver
from common.base_page import BasePage
from common.logpy import LogHandler
from common.pageObject.aiologinpage import AioLogin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from conf import readconfig
from common.global_element import GlobalElements


class HomePage(AioLogin):
    global logg
    logg = LogHandler().getlog()
    e_main = GlobalElements.mainpage
    e_common = GlobalElements.common

    # devgrp_name_click = By.CSS_SELECTOR,"td.has-split[title="+groupname+"]"
    def init_home_page(self):
        self.correct_login()
        logg.info("init home page")
        # self.click_btn(*self.check_default)

    def click_service_overview(self):
        self.click_btn(*self.e_main.service_overview_menu)
        sleep(1)

    def click_store_menu(self):
        '''
        点击 云存储
        '''
        self.click_btn(*self.e_main.store_menu)
        sleep(1)

    def click_setting_menu(self):
        """
        点击 设置
        :return:
        """
        self.click_btn(*self.e_main.setting_menu)
        sleep(1)

    def click_service_manager_menu(self):
        self.click_service_overview()
        self.click_store_menu()
        return self.click_btn(*self.e_main.service_manager_menu)

    def click_client_manager_menu(self):
        self.click_service_overview()
        self.click_store_menu()
        return self.click_btn(*self.e_main.client_manager_menu)

    def click_devgrp_manager_menu(self):
        self.click_service_overview()
        self.click_store_menu()
        return self.click_btn(*self.e_main.devgrp_manager_menu)

    def click_block_manager_menu(self):
        """
        点击 块设备管理界面
        :return:
        """
        logg.info("块设备管理 页面")
        self.click_service_overview()
        self.click_store_menu()
        return self.click_btn(*self.e_main.block_manager_menu)

    def click_file_manager_menu(self):
        self.click_service_overview()
        self.click_store_menu()
        return self.click_btn(*self.e_main.file_manager_menu)

    def click_perm_manager_menu(self):
        logg.info("权限管理 页面")
        self.click_service_overview()
        self.click_store_menu()
        return self.click_btn(*self.e_main.perm_manager_menu)

    def click_senior_manager_menu(self):
        self.click_service_overview()
        self.click_store_menu()
        return self.click_btn(*self.e_main.senior_manager_menu)

    def click_log_menu(self):
        logg.info("日志管理 页面")
        self.click_service_overview()
        self.click_store_menu()
        return self.click_btn(*self.e_main.log_menu)


if __name__ == '__main__':
    test = HomePage(webdriver.Chrome())
    test.init_home_page()
    test.click_store_menu()
    test.click_block_manager_menu()
    test.click_log_menu()
    test.click_perm_manager_menu()
    test.brower_close()
