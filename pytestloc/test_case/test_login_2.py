from time import sleep
from ddt import data,ddt,unpack
from common.logpy import LogHandler
from data.readexcel import  ReadExcel
from common.pageObject import aiologinpage
from common.base_page import BasePage
import unittest,pytest
from selenium import webdriver
# t=webdriver.Chrome()

class TestLoginCheck(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # global test
        global logg
        logg = LogHandler().getlog()
        cls.test = aiologinpage.AioLogin(webdriver.Chrome())
        getandcheck = cls.test.get_conf_url()
        if not getandcheck:
            TestLoginCheck.tearDownClass()
            logg.error("进入主页失败，err:14001")
            return SystemExit(14001)

    @classmethod
    def tearDownClass(cls):
        TestLoginCheck().test.brower_close()
        pass

    def testcase1(self):
        username = 'adminxx1'
        passwd = 'ad'
        result = False
        self.test.set_username(username)
        self.test.set_password(passwd)
        self.test.type_login_btn()
        # 断言登录结果和预期结果是否一致
        # self.assertEqual(self.test.checkLoginResult(result),True,msg="login_test fail")
        self.assertTrue(self.test.check_login_result(result),
                        msg="\r  login_test fail \r  username :%s \r    passwd : %s " %(username,passwd))
    def testcase2(self):
        username = 'xx2'
        passwd = 'ad22'
        result = False
        self.test.set_username(username)
        self.test.set_password(passwd)
        self.test.type_login_btn()
        # 断言登录结果和预期结果是否一致
        # self.assertEqual(self.test.checkLoginResult(result),True,msg="login_test fail")
        self.assertTrue(self.test.check_login_result(result),
                        msg="\r  login_test fail \r  username :%s \r    passwd : %s " %(username,passwd))

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
    unittest.main()
