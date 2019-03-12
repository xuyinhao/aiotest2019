from conf import readconfig
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.logpy import LogHandler
import sys,time
#一个登陆页面的BasePage
class BasePage():
    global logg
    logg = LogHandler().logger
    # def __init__(self,driver=webdriver.Chrome()):
    def __init__(self,driver):
        self.wd = driver
        self.wd.implicitly_wait(5)
        self.url = self.server_url_conf()
    #浏览器行为
    def get_conf_url(self):
        self.wd.get(self.url)
        self.wd.maximize_window()
        logg.debug("enter conf_url : " + str(self.url))

    def brower_close(self):
        return self.wd.quit()
    def brower_setwindowssize(self,width,height,windowHandle='current'):
        self.wd.set_window_size(width,height,windowHandle)
    def brower_fresh(self):
        self.wd.refresh()
    def brower_forward(self):
        self.wd.forward()
    def brower_backward(self):
        self.wd.back()

    #定位
    def find_web_element(self,*loc):
        #self.wd.find_element(*loc)
        return self.wd.find_element(*loc)

    #元素操作
    def type_text(self,loc,text):
        return  self.wd.find_element(*loc).send_keys(text)
    def clear_text(self,*loc):
        return self.wd.find_element(*loc).clear()
    def click_btn(self,*loc):
        return self.wd.find_element(*loc).click()

    #获取信息行为
    def get_web_url(self):
        return self.wd.current_url
    def get_title(self):
        return  self.wd.title
    def check_element_isexist(self,*loc):
        flag = False
        try:
            self.find_web_element(*loc)
            flag = True
        except Exception as e:
            flag = False
        return flag
    def check_element_isdisplayed(self,*loc):
        flag = True
        try:
            self.find_web_element(*loc).is_displayed()
        except:
            flag = False
        return flag
    @classmethod
    def server_url_conf(cls):
        cls.host = readconfig.ReadConfig().getserver('host')
        cls.port = readconfig.ReadConfig().getserver('port')
        urlvalue = cls.host + ":" + cls.port

        return urlvalue

if __name__ == '__main__':
    test = BasePage(webdriver.Chrome())
    test.get_conf_url()
   # print(test.getWebUrl())
  #  print(test.getTitle())
    print(test.check_element_isdisplayed(By.CLASS_NAME,"error-tip"))
