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
    password_loc = (By.CLASS_NAME, "password-text")
    login_loc = (By.CLASS_NAME, "login-btn")
    check_login_loc = (By.CLASS_NAME,"error-tip")
    elements = [username_loc,password_loc,login_loc,check_login_loc]
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

    def type_login_btn(self):
        self.click_btn(*self.login_loc)
        sleep(0.1)

    def check_login_result(self,testcase_login_result):
        err_class_result = self.check_element_isexist(*self.check_login_loc)
        flag = None
        if err_class_result == False:
            flag = True         #不存在元素，则页面已经跳转。登录成功
        if err_class_result == True:
            flag = False

        if flag == testcase_login_result:
            result = True       #登录结果和预期结果一致，则返回成功
        else:
            result = False
        # self.logg.info("check : " + str(flag) + " " + str(testcase_login_result) + " "
        #                + "result : " + str(result))
        return result
    def correct_userpasswd_conf(self):
        self.tusername = readconfig.ReadConfig().get_configinfo('user','tuser')
        self.tpassword = readconfig.ReadConfig().get_configinfo('user','tpassword')
        self.urlvalue = (self.tusername,self.tpassword)
        return self.urlvalue
    def correct_login(self):
        self.get_conf_url()
        self.userpasswd = self.correct_userpasswd_conf()
        self.set_username(self.userpasswd[0])
        self.set_password(self.userpasswd[1])
        self.type_login_btn()



if __name__ == '__main__':
    test=AioLogin(webdriver.Chrome())
    test.correct_login()
    # test.get_conf_url()
    # test.set_username('admin')
    # test.set_password('admin1')
    # test.type_login_btn()
    # print(test.check_login_result(False))
    # test.set_username('xx')
    # test.set_password('admixxn1')
    # test.type_login_btn()
    # print(test.check_login_result(True))
    # test.brower_close()


