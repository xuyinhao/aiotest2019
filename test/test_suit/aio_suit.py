from common import htmlrunner
from test.testcase import aiologin
import unittest
if __name__ == '__main__':
    runner = htmlrunner.GenHtmlReport().reportgen('aio-1','no description')

    st1 = unittest.TestLoader().loadTestsFromModule(aiologin)

    runner.run(st1)

    #创建添加class
    # st = unittest.TestSuite(map(TestLoginCheck,['testcase1','testcase2']))
    # st2 = unittest.makeSuite(TestLogin)
    # st3 = unittest.TestSuite()
    # st3.addTest(unittest.makeSuite(TestLogin)
    # st4 = unittest.TestSuite()
    # st4.addTests(map(TestLoginCheck,['testcase1','testcase2']))
    # st4.addTest(unittest.makeSuite(TestLogin))
    # runner.run(st4)
    # st5 = unittest.TestSuite()
    # st5.addTest(TestLoginCheck('testcase2'))

