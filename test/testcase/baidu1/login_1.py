import unittest
from test.pageObject import basepage
from common.browser import browser
from common.htmlrunner import reportgen
from ddt import data,ddt
from time import sleep

@ddt
class Test_Search2(unittest.TestCase):
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
        cls.driver.close()
        print('quit')
        pass

    global test_info
    test_info=[]
    for i in range(3):
        test_info.append(i)

    @data(*test_info)
    def test_b_search(self,test_info):
        '''Test test_info'''
        print('data '+str(test_info))
      #  self.driver=browser()
      #   opendb=self.test_a_open()
        try:
            self.opendb.search(test_info)
            self.opendb.click_bdyx()
            sleep(1)
            print(str(test_info),self.driver.title)
           # assert "2" not in self.driver.title
            # self.opendb.clear()
            sleep(2)
        except  Exception as err:
            print(err)
        finally:
            print('end')
            #self.driver.quit()

if __name__ == '__main__':
    unittest.main()

