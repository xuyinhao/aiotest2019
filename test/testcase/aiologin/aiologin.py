from time import sleep
from ddt import data,ddt,unpack
from common.browser import browser
from common.pageObject import aiologinpage
from common.base_page import BasePage
import unittest
from selenium import webdriver

@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # global test
        cls.test = aiologinpage.AioLogin(webdriver.Chrome())
        cls.test.get_url()
       # print('start TestSearch')
    @classmethod
    def tearDownClass(cls):
        TestLogin().test.brower_quit()
        pass
    @data(('admin','admin1',False),('admin','admin',True))
    @unpack
    def testcase2(self,username,passwd,result):
        self.test.set_username(username)
        self.test.set_password(passwd)
        self.test.type_login_btn()
       # self.assertEqual(self.test.get_title(),u"主页")
    #测试一下 wd
    # def testcase3(self):
    #     sleep(2)
    #     self.test.wd.find_element_by_name('username').clear()
    #     sleep(2)
    #     self.test.wd.find_element_by_class_name('password-text').clear()
    #     sleep(2)
    #     self.test.wd.quit()

if __name__ == '__main__':
    unittest.main()