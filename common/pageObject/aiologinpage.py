# PageObject（页面对象），
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
from common.global_element import GlobalElements


class AioLogin(BasePage):
    global logg
    logg = LogHandler().getlog()
    e_login = GlobalElements.login

    def get_and_check_server_url(self, OEMtitle=None):
        self.get_conf_url()
        sleep(3)
        if not OEMtitle:
            if "" != self.get_title():
                return False
        elif OEMtitle != self.get_title():
            return False
        return True

    def set_username(self, username):
        # self.find_element(*self.username_loc).clear()
        # self.find_element(*self.username_loc).send_keys(username)
        self.clear_text(*self.e_login.username_loc)
        self.type_text(self.e_login.username_loc, username)
        logg.info('Enter username: ' + username)
        sleep(0.1)

    def set_password(self, password):
        self.clear_text(*self.e_login.password_loc)
        self.type_text(self.e_login.password_loc, password)
        logg.info('Enter password: ' + password)
        sleep(0.1)

    def type_login_btn(self, OEM=None):
        if OEM:
            flag = self.click_btn(*self.e_login.login_loc_oem)
        else:
            flag = self.click_btn(*self.e_login.login_loc)
        sleep(0.1)
        return flag

    def _check_login_ok(self):
        ok_class_result = False
        ok_class_result = self.check_element_isexist(self.e_login.log_menu)
        logg.debug("__check login " + str(ok_class_result))
        sleep(0.2)
        # self.insert_success_img('check_login_ok')
        return ok_class_result

    def _check_login_fail(self):
        fail_class_result = False
        fail_class_result = self.check_element_isexist(self.e_login.login_loc)
        logg.debug("__check not login" + str(fail_class_result))
        sleep(0.1)
        return fail_class_result

    def check_login_result(self, testcase_login_expected_result):
        flag = None
        if testcase_login_expected_result:
            if self._check_login_ok():
                flag = True
                self.insert_success_img("登录成功")
            else:
                flag = False
                self.insert_error_img("登录失败")
        else:
            if self._check_login_fail():
                flag = True
                self.insert_success_img('登录用例 检查成功')
            else:
                flag = False
                self.insert_error_img('登录用例 检查失败')
        return flag

    def __correct_userpasswd_conf(self):
        self.tusername = readconfig.ReadConfig().get_configinfo('user', 'tuser')
        self.tpassword = readconfig.ReadConfig().get_configinfo('user', 'tpassword')
        self.urlvalue = (self.tusername, self.tpassword)
        return self.urlvalue

    def correct_login(self, OEM=None):
        self.get_conf_url()
        self.userpasswd = self.__correct_userpasswd_conf()
        self.set_username(self.userpasswd[0])
        self.set_password(self.userpasswd[1])
        login_result = self.type_login_btn(OEM=OEM)
        return login_result


if __name__ == '__main__':
    # test=AioLogin(webdriver.Chrome(),"http://13.10.47.6:8088")
    # test.correct_login(OEM=True)
    test = AioLogin(webdriver.Chrome())
    test.get_conf_url()
    test.set_username('admin')
    test.set_password('admin')
    test.type_login_btn()
    # print(test.check_login_result(False))
    # test.set_username('xx')
    # test.set_password('admixxn1')
    # test.type_login_btn()
    # print(test.check_login_result(True))
    # test.brower_close()
