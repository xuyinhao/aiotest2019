#PageObject（页面对象），
# 简单点说就是把界面定位和业务操作分开。
# 这个框架主要是把UI自动化分为三层：对象库层、操作层和业务层。
from selenium import webdriver
from common.base_page import BasePage
from common.logpy import LogHandler
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from conf import readconfig
import logging

class AioLogin(BasePage):
    global logg
    logg = LogHandler().getlog()

    username_loc = (By.NAME, "username")
    password_loc = (By.CSS_SELECTOR, "input[type='password']")
    login_loc = (By.CLASS_NAME, "login-btn")
    login_loc_oem = (By.ID,"submit")
    check_login_loc = (By.CLASS_NAME,"error-tip")
    elements = [username_loc,password_loc,login_loc,check_login_loc]
    log_menu = (By.CSS_SELECTOR,"[name='log']")
    logg.debug(elements)
    def set_username(self,username):
       # self.find_element(*self.username_loc).clear()
        #self.find_element(*self.username_loc).send_keys(username)
        self.clear_text(*self.username_loc)
        self.type_text(self.username_loc,username)
        logg.info('Enter username: ' + username)
        sleep(0.1)

    def set_password(self,password):
        self.clear_text(*self.password_loc)
        self.type_text(self.password_loc,password)
        logg.info('Enter password: ' + password)
        sleep(0.1)

    def type_login_btn(self,OEM=None):
        if OEM:
            self.click_btn(*self.login_loc_oem)
        else:
            self.click_btn(*self.login_loc)
        sleep(0.1)
        return  self._check_login_ok()

    def _check_login_ok(self):
        ok_class_result = self.check_element_isexist(self.log_menu)
        logg.debug("_check " + str(ok_class_result))
        sleep(0.5)
        # self.insert_success_img('check_login_ok')
        return ok_class_result

    def check_login_result(self,testcase_login_expected_result):

        flag = self._check_login_ok()
        if flag == testcase_login_expected_result:
            result = True       #登录结果和预期结果一致，则返回成功
            if True == testcase_login_expected_result:
                self.insert_success_img("登录成功")
            else:
                self.insert_success_img('登录用例 检查成功')
        else:
            result = False
            self.insert_error_img("登录 检查失败")
            logg.error("check : %s %s result : %s"
                       % (str(flag),str(testcase_login_expected_result),str(result)))
        return result
    def correct_userpasswd_conf(self):
        self.tusername = readconfig.ReadConfig().get_configinfo('user','tuser')
        self.tpassword = readconfig.ReadConfig().get_configinfo('user','tpassword')
        self.urlvalue = (self.tusername,self.tpassword)
        return self.urlvalue
    def correct_login(self,OEM=None):
        self.get_conf_url()
        self.userpasswd = self.correct_userpasswd_conf()
        self.set_username(self.userpasswd[0])
        self.set_password(self.userpasswd[1])
        login_result = self.type_login_btn(OEM=OEM)
        return login_result


if __name__ == '__main__':
    # test=AioLogin(webdriver.Chrome(),"http://13.10.47.6:8088")
    # test.correct_login(OEM=True)
    test=AioLogin(webdriver.Chrome())
    test.get_conf_url()
    test.set_username('admin')
    test.set_password('admin1')
    test.type_login_btn()
    # print(test.check_login_result(False))
    # test.set_username('xx')
    # test.set_password('admixxn1')
    # test.type_login_btn()
    # print(test.check_login_result(True))
    # test.brower_close()


