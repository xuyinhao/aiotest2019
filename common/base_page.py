from conf import readconfig
from selenium import webdriver
import sys,time
#一个登陆页面的BasePage
class BasePage():

    def __init__(self,driver):
        self.wd = driver
        self.url = self.urlconf()
    #定义定义open方法，调用_open()进行打开

    def get_url(self):
        # self.driver = self.wd
       # self.timeout = 30
        print("open")
        self.wd.get(self.url)
        self.wd.maximize_window()

    #定位方法封装
    def find_element(self,*loc):
        #self.wd.find_element(*loc)
        return self.wd.find_element(*loc)
    def type_text(self,loc,text):
        return  self.wd.find_element(*loc).send_keys(text)
    def clear_text(self,*loc):
        return self.wd.find_element(*loc).clear()
    def click_btn(self,*loc):
        return self.wd.find_element(*loc).click()
    def brower_quit(self):
        return self.wd.quit()
    def get_title(self):
        return  self.wd.title
    @classmethod
    def urlconf(cls):
        cls.host = readconfig.ReadConfig().getserver('host')
        cls.port = readconfig.ReadConfig().getserver('port')
        urlvalue = cls.host + ":" + cls.port
        return urlvalue
    # @classmethod
    # def brower(cls):
    #     bw = readconfig.ReadConfig().getbw()
    #     if  bw == "chrome":
    #         bw = webdriver.Chrome()
    #     return  bw

if __name__ == '__main__':
    test = BasePage(webdriver.Chrome())
    test.open()
    time.sleep(2)
    test.wd.quit()

