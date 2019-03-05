import unittest
from test.pageObject import basepage
from common.browser import browser
from ddt import data,ddt
from time import sleep

class Test_Search(unittest.TestCase):
    def setUp(self):
        self.driver=browser()
        print('start TestSearch')
    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.testsearch(arg1)
        return func

    def testsearch(self,tests):
      #  self.driver=browser()
        try:
            opendb=basepage.BaiduPage(self.driver)
            opendb.open()
            opendb.search(tests)
            opendb.click_bdyx()
           # sleep(0.2)
            opendb.clear()
            #sleep(2)
        except  Exception as err:
            print(err)
        finally:
            print('end')
            #self.driver.quit()



    # def test_search(self):
    #     opendb=basepage.BaiduPage(self.driver)
    #     opendb.open()
    #     opendb.search('www')
    #     opendb.click_bdyx()
    #     sleep(0.2)
    #     opendb.clear()

    def tearDown(self):
        self.driver.quit()
        pass

def __generateTestCases():
    for i in range(0,1):
        setattr(Test_Search,'test_func_%s' %(i),
                Test_Search.getTestFunc(i))
__generateTestCases()
if __name__ == '__main__':

    unittest.main()

