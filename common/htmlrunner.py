import HTMLTestRunner
def reportgen(report_path,title,descrip):
    report_path="../report/report.html"
    fp=open(report_path,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                         title=u'自动化测试-报告',
                                         description=u'用例执行情况')
    return runner
if __name__ == '__main__':
   reportgen()
