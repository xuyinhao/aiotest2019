#导入HTMLTestRunner的包
import HTMLTestRunner
#导入test_login的包，执行测试用例时需使用
from test.testcase.baidu1.login_1 import *
from test.testcase.baidu2.write_2 import *
import time
filename='../../report/report'+str(time.time())+'.html'
#开始执行
if __name__ == '__main__':
    #以wb(可写的二进制文件)形式，打开文件，若文件不存在，则先执行创建，再执行打开
    fp = open(filename, 'wb')
    #调用HTMLTestRunner生成报告
    runner = HTMLTestRunner.HTMLTestRunner(
        # 指定测试报告的文件
        stream=fp,
        # 测试报告的标题
        title=u"百度搜索测试",
        # 测试报告的副标题
        description=u'用例执行情况（e）'
    )
    #执行用例
    #创建一个测试集合
    test_suite=unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(Test_Search2))
    test_suite.addTest(unittest.makeSuite(Test_Search4))
    runner.run(test_suite)
