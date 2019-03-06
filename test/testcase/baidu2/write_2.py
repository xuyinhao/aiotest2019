import unittest
from time import sleep

from ddt import data,ddt

from common.browser import browser
from common.pageObject import basepage


@ddt
class Test_Search4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver=browser()
        cls.driver=driver
        driver.implicitly_wait(30)
        print('test_open')
        opendb = basepage.BaiduPage(driver)
        opendb.open()
        cls.opendb=opendb
       # print('start TestSearch')
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print('quit')
        pass

    global test_info
    test_info=[]
    for i in range(2):
        test_info.append('第四'+str(i))

    @data(*test_info)
    def test_c_search(self,test_info):
        '''Test test_info'''
        print('data '+str(test_info))
      #  self.driver=browser()
      #   opendb=self.test_a_open()
        try:
            self.opendb.search(test_info)
            self.opendb.click_bdyx()
            sleep(0.2)
            self.opendb.clear()
            sleep(2)
        except  Exception as err:
            print(err)
        finally:
            print('end')
            #self.driver.quit()

if __name__ == '__main__':
    unittest.main()

