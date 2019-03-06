from conf import readconfig
from selenium import webdriver
import sys,time
#一个登陆页面的BasePage
class BasePage():
    def __init__(self,driver=webdriver):
        self.driver = webdriver
    #定义定义open方法，调用_open()进行打开
    def open(self):
        self.url = self.urlconf()
        if self.brower() == "chrome":
            print("chrome")
            self.wd = self.driver.Chrome()
        elif self.brower() == "firefox":
            print("firefox")
            self.wd = self.driver.Firefox()
        else:
            print("Unknow")
            sys.exit(-1)
        # self.driver = self.wd
        self.timeout = 30
        self.wd.get(self.url)
        self.wd.maximize_window()

    #定位方法封装
    def find_element(self,*loc):
        return self.wd.find_element(*loc)

    def urlconf(self):
        self.host = readconfig.ReadConfig().getserver('host')
        self.port = readconfig.ReadConfig().getserver('port')
        urlvalue = self.host + ":" + self.port
        return urlvalue
    def brower(self):
        self.bw = readconfig.ReadConfig().getbw()
        return  self.bw

if __name__ == '__main__':
    test = BasePage()
    test.open()
    time.sleep(2)
    test.wd.quit()

