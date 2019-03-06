#PageObject（页面对象），
# 简单点说就是把界面定位和业务操作分开。
# 这个框架主要是把UI自动化分为三层：对象库层、操作层和业务层。
from selenium import webdriver
from common.browser import browser
from common.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time  import sleep
from conf import readconfig

class AioLogin(BasePage):
    username_loc = (By.NAME, "username")
    password_loc = (By.CLASS_NAME, "password-text")
    login_loc = (By.CLASS_NAME, "login-btn")

    def set_username(self,username):
       # self.find_element(*self.username_loc).clear()
        #self.find_element(*self.username_loc).send_keys(username)
        self.clear_text(*self.username_loc)
        self.type_text(self.username_loc,username)

    def set_password(self,password):
        self.clear_text(*self.password_loc)
        self.type_text(self.password_loc,password)

    def type_login_btn(self):
        self.click_btn(*self.login_loc)


if __name__ == '__main__':
    test=AioLogin(webdriver.Chrome())
    test.get_url()
    test.set_username('admin')
    test.set_password('admin')
    test.type_login_btn()


