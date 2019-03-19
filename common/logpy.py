import logging,time
from conf import readconfig
import os.path
#studyby: https://www.cnblogs.com/CJOKER/p/8295272.html
# logging.basicConfig(level = logging.NOTSET,
#                     format='%(asctime)s_%(name)s_[%(levelname)s] : %(message)s')
#NOSET: 全部日志 ； DEBUG，INFO,WARNING,ERROR,CRITICAL
#基本配置
#logging.basicConfig(level = logging.NOTSET)
# #logger是logging模块的主体
# #1.提供日志接口，2 判断级别过滤 3，不同级别分发到不同的handler

class LogHandler():
    def __init__(self,logger=None):
        # print(logger)
        self.logging = logging
        #1.c创建logger
        self.logger = self.logging.getLogger(logger)
        self.logger.setLevel(self.logging.NOTSET) #log级别总开关
        formatter = self.logging.Formatter('%(asctime)s_%(threadName)s_[%(levelname)s] : %(message)s')

        #2 创建handler

        if not self.logger.handlers:
            timestr = time.strftime('%Y%m%d%H',time.localtime(time.time()))
            logpypath = os.path.abspath(__file__)
            logname = logpypath + "/../../log/"+ "stdout"+ timestr + ".log"
            logpath = os.path.join(logname)
            self.filehandler = self.logging.FileHandler(logpath,mode='a+',encoding='utf-8')
            self.filehandler.setLevel(self.logging.INFO)  #输出到file的log等级的开关
            self.filehandler.setFormatter(formatter)

            self.streamhandler = self.logging.StreamHandler()
            self.streamhandler.setLevel(self.get_logcfg())
            self.streamhandler.setFormatter(formatter)
            # 给logger添加handler
            self.logger.addHandler(self.filehandler)
            self.logger.addHandler(self.streamhandler)
            # self.logger.removeHandler(self.filehandler)
            # self.logger.removeHandler(self.streamhandler)
            # self.filehandler.close()
            # self.streamhandler.close()

    @staticmethod
    def get_logcfg():
        cfgfile = readconfig.ReadConfig()
        consolelevel = cfgfile.get_configinfo('log','console')
        console_log_level=logging.INFO
        if consolelevel == "NOSET":
            console_log_level = logging.NOTSET
        if consolelevel == "DEBUG":
            console_log_level = logging.DEBUG
        if consolelevel == "INFO":
            console_log_level = logging.INFO
        if consolelevel == "WARNING":
            console_log_level = logging.WARNING
        if consolelevel == "ERROR":
            console_log_level = logging.ERROR
        return console_log_level
    def getlog(self):
        return self.logger
if __name__ == '__main__':
    a=LogHandler().getlog()
    n=LogHandler().getlog()
    a.error('这是debug')
    # a.logger.info("这是info")
    # a.logger.warning("这是warning")
    # a.logger.error("这是error")
    # a.logger.critical("这是cri")
    # print(a,n)
    #异常捕获 日志记录
    try:
        f = open('ff','r')
    except Exception as e:
        a.error('failed : ',exc_info = True)
    finally:
        pass





