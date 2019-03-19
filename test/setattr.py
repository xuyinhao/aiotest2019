#coding:utf-8
import unittest
from common.logproc.logger import *
from common.logproc.logresult import logresult
class TestCase(unittest.TestCase):
    def setUp(self):
        print('stt')
        pass

    @loggering(level='INFO')
    def action(self,arg1,arg2):
        # print(arg1,arg2)
        arg1=arg1
        tname='测试用例：'+self._testMethodName+': '
        logresult().logcmp(tname,arg1,arg2)

    @staticmethod
    def getTestFunc(arg1,arg2):
        def func(self):
            self.action(arg1,arg2)
        return  func

def __generateTestCases():
    for i in range(0,10):
        setattr(TestCase,'test_func_%s_%s' %(i,i),
                TestCase.getTestFunc(i,i))
__generateTestCases()

# print(TestCase.__dict__)
if __name__ =='__main__':
    unittest.main()
#test
