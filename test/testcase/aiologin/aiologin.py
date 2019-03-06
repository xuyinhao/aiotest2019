from time import sleep
from ddt import data,ddt,unpack
from common.browser import browser
from common.pageObject import basepage

@ddt
class Test_Search2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=browser()
      #  cls.driver=driver
        cls.driver.implicitly_wait(30)

        cls.opendb = basepage.BaiduPage(cls.driver)
        cls.opendb.open()
        cls.opendb=cls.opendb
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
            self.opendb.clear()
            self.opendb.search(test_info)
            self.opendb.click_bdyx()
            sleep(1)
            print(str(test_info),self.driver.title)

            self.assertEqual(u'2_百度搜索',self.driver.title,'err_msg：check_title')
            # except AssertionError as msg:
            #     print(msg)
            # self.opendb.clear()
            sleep(2)
        finally:
            print('end')
            #self.driver.quit()

if __name__ == '__main__':
    unittest.main()