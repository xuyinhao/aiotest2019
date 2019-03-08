from time import sleep
from ddt import data,ddt,unpack
from data.readexcel import  ReadExcel
from common.pageObject import aiologinpage
from common.base_page import BasePage
import unittest
from selenium import webdriver
# t=webdriver.Chrome()


@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # global test
        cls.test = aiologinpage.AioLogin(webdriver.Chrome())
        cls.test.getConfUrl()

       # print('start TestSearch')
    @classmethod
    def tearDownClass(cls):
        TestLogin().test.browerClose()
        pass
    logindata = ReadExcel().getValue('login')
    @data(*logindata)
    @unpack
    def testcase2(self,username,passwd,result):
        self.test.setUsername(username)
        self.test.setPassword(passwd)
        self.test.typeLoginBtn()
        # 断言登录结果和预期结果是否一致
        # self.assertEqual(self.test.checkLoginResult(result),True,msg="login_test fail")
        self.assertTrue(self.test.checkLoginResult(result),
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
