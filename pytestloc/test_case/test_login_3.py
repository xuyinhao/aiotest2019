# from time import sleep
# from ddt import data,ddt,unpack
# from common.logpy import LogHandler
# from data.readexcel import  ReadExcel
from common.pageObject import aiologinpage
# from common.base_page import BasePage
import pytest
import allure
# import sys,os
import logging
from selenium import webdriver
# t=webdri

@allure.feature('测试登录_3')
class TestLoginCheck():

    def setup_class(self):
        # global test
        global logg
        logg = logging.getLogger()
        self.test = aiologinpage.AioLogin(webdriver.Chrome())
        getandcheck = self.test.get_and_check_server_url()
        if not getandcheck:
            TestLoginCheck().teardown_class()
            logg.error("进入主页失败，err:14001")
            return SystemExit(14001)

    def teardown_class(self):
        self.test.brower_close()
        pass

    @allure.story('测试失败登录Case')
    def testcase1(self):
        username = 'adminxx1'
        passwd = 'ad'
        result = False
        self.test.set_username(username)
        self.test.set_password(passwd)
        self.test.type_login_btn()
        # 断言登录结果和预期结果是否一致
        # self.assertEqual(self.test.checkLoginResult(result),True,msg="login_test fail")
        assert self.test.check_login_result(result)
                        # msg="\r  login_test fail \r  username :%s \r    passwd : %s " %(username,passwd))

    @allure.story('测试成功登录case')
    @allure.severity('critical')
    # @allure.step("账户密码期望结果：{0},{1},{2}")
    #test2
    def testcase2(self):
        username = 'xx2'
        passwd = 'ad22'
        result = False
        self.test.set_username(username)
        self.test.set_password(passwd)
        self.test.type_login_btn()
        # 断言登录结果和预期结果是否一致
        # self.assertEqual(self.test.checkLoginResult(result),True,msg="login_test fail")
        assert self.test.check_login_result(result)
                        # msg="\r  login_test fail \r  username :%s \r    passwd : %s " %(username,passwd))

       # self.assertEqual(self.test.get_title(),u"主页")
    #测试一下 self.wd方法
    # def testcase3(self):
    #     sleep(2)
    #     self.test.wd.find_element_by_name('username').clear()
    #     sleep(2)
    #     self.test.wd.find_element_by_class_name('password-text').clear()
    #     sleep(2)
    #     self.test.wd.quit()

if __name__ == '__main__':
    # pytest.main(["-s",os.path.basename(__file__)])
    pytest.main(["-s","test_login_3.py"])
