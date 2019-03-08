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
    username_loc = (By.NAME, "username")
    password_loc = (By.CLASS_NAME, "password-text")
    login_loc = (By.CLASS_NAME, "login-btn")
    check_login_loc = (By.CLASS_NAME,"error-tip")

    logg = LogHandler().logger
    def setUsername(self,username):
       # self.find_element(*self.username_loc).clear()
        #self.find_element(*self.username_loc).send_keys(username)
        self.clearText(*self.username_loc)
        self.typeText(self.username_loc,username)
        self.logg.error('Enter username: ' + username)
        sleep(0.1)

    def setPassword(self,password):
        self.clearText(*self.password_loc)
        self.typeText(self.password_loc,password)
        self.logg.error('Enter password: ' + password)
        sleep(0.1)

    def typeLoginBtn(self):
        self.clickBtn(*self.login_loc)
        sleep(0.1)

    def checkLoginResult(self,testcase_login_result):
        err_class_result = self.checkElementExist(*self.check_login_loc)
        flag = None
        if err_class_result == False:
            flag = True         #不存在元素，则页面已经跳转。登录成功
        if err_class_result == True:
            flag = False

        if flag == testcase_login_result:
            result = True       #登录结果和预期结果一致，则返回成功
        else:
            result = False
        self.logg.info("check : " + str(flag) + " " + str(testcase_login_result) + " "
                       + "result : " + str(result))
        return result
    @staticmethod
    def okUserPasswdConf():
        tusername = readconfig.ReadConfig().getConfigInfo('user','tuser')
        tpassword = readconfig.ReadConfig().getConfigInfo('user','tpassword')
        urlvalue = (tusername,tpassword)
        return urlvalue
    def okLogin(self):
        userpasswd = self.okUserPasswdConf()
        self.setUsername(userpasswd[0])
        self.setPassword(userpasswd[1])
        self.typeLoginBtn()


if __name__ == '__main__':
    test=AioLogin(webdriver.Chrome())
    test.getConfUrl()
    test.setUsername('admin')
    test.setPassword('admin1')
    test.typeLoginBtn()
    print(test.checkLoginResult(False))
    test.setUsername('xx')
    test.setPassword('admixxn1')
    test.typeLoginBtn()
    print(test.checkLoginResult(True))
    test.browerClose()


