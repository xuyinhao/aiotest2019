from selenium import webdriver
from common.base_page import BasePage
from common.logpy import LogHandler
from common.pageObject.aiologinpage import AioLogin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from conf import readconfig

class DevgrpPage(BasePage):
    global logg
    logg = LogHandler().getlog()
    store_menu = (By.CSS_SELECTOR,"div.menu-content[data-title='云存储']")
    devgrp_menu = (By.CSS_SELECTOR,"div.menu-content[data-title='设备分组管理']")
    check_default = (By.CSS_SELECTOR,"td.has-split[title='default']")
    create_devgrp_loc = (By.NAME,"create-group")
    input_devgrp_name_loc = (By.CSS_SELECTOR,".mb-body >form:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)")
    input_devgrp_name_confirm = (By.CLASS_NAME,"custom-button")
    def init_web(self):
        AioLogin(self.wd).correct_login()
        self.click_btn(*self.store_menu)
        self.click_btn(*self.devgrp_menu)
        logg.info("devgroup wait 2s")
        sleep(2)
        # self.click_btn(*self.check_default)
        if not self.check_groupname_result("default"):
            logg.error('initweb check default grp : error' )
            self.brower_close()
    def create_devgrp(self,devgrpname):
        flag = True
        self.click_btn(*self.create_devgrp_loc)
        self.type_text(self.input_devgrp_name_loc,devgrpname)
        self.click_btn(*self.input_devgrp_name_confirm)
        print(*self.input_devgrp_name_confirm)
        if  self.check_groupname_result(devgrpname):
            logg.info('initweb check %s grp : error ' %(devgrpname))
            flag = False
        return flag

    def check_groupname_result(self,groupname):
        flag = False
        if self.check_element_isexist(By.CSS_SELECTOR,"td.has-split[title="+groupname+"]"):
            flag = True
        logg.info("%s group exist is : %s" %(groupname,str(flag)))
        return  flag

if __name__ == '__main__':
    test = DevgrpPage(webdriver.Chrome())
    test.init_web()
    for i in range(11,12):
        name = "dev"+str(i)
        ret = test.create_devgrp(name)
        if ret :
            logg.info(name + "pass")
        else:
            logg.error(name + "error")

