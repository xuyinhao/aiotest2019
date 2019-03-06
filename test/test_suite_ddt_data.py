import unittest
# from common import loggering
from ddt import data,ddt

@ddt
class testProductTestCase(unittest.TestCase):
    global test_name
    def setUp(self):
        print("starting……")
        pass
    def tearDown(self):
        print("Ended...")
        pass
    test_name=[]
    for testnum in range(1,4):
        test_data=testnum
        test_name.append(test_data)
    # print(*test_name)
    #
        #多个装饰器 应用时顺序是相反的
    @data(*test_name)
    # @loggering(level='INFO2')
    def testfloat(self,test_name):
        print(test_name)

if __name__ == '__main__':
    unittest.main()



