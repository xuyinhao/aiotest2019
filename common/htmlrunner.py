import HTMLTestRunner
import os
class GenHtmlReport():
    '''
    gen html report
    titlename,description_info
    '''
    def __init__(self):
        '''
        gen html report
        titlename,description_info
        '''
        pass

    def reportgen(self,titlename,descrip):
        import time
        date = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        filepath = os.path.abspath(__file__)
        report_path = os.path.join(filepath+r"\..\..\log\reportlog"+ date +".html")

        fp=open(report_path,"wb")
        runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                             title=titlename,
                                             description=descrip)
        return runner
if __name__ == '__main__':
   test = GenHtmlReport()
   print(test.reportgen(u'AIO-登录测试—test',u'mei没有'))

