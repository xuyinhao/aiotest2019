from time import sleep
from ddt import data,ddt,unpack
from data.readexcel import  ReadExcel
from common.pageObject import aiologinpage
from common.base_page import BasePage
import unittest
from selenium import webdriver
from common.logpy import LogHandler
import allure
# t=webdriver.Chrome()

@allure.feature("测试用例_1")
@ddt
class TestLogin(unittest.TestCase):
    global logg
    logg = LogHandler().getlog()
    
    @classmethod
    def setUpClass(cls):
        cls.test = aiologinpage.AioLogin(webdriver.Chrome())
        getandcheck = cls.test.get_and_check_server_url()
        if not getandcheck:
            TestLogin.tearDownClass()
            logg.error("进入主页失败，err:14001")
            return exit(14001)
       # print('start TestSearch')
    @classmethod
    def tearDownClass(cls):
        # TestLogin().logg.info("brower quit")
        TestLogin().test.brower_close()
        pass
    logindata = ReadExcel().getValue('login')
    @allure.story("测-2")
    @data(*logindata)
    @unpack
    def test_case2(self,username,passwd,result):
        logg.info(username+" " + passwd +" " +str(result))
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
