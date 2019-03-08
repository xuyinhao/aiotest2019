from conf import readconfig
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys,time
#一个登陆页面的BasePage
class BasePage():
    # def __init__(self,driver=webdriver.Chrome()):
    def __init__(self,driver):
        self.wd = driver
        self.url = self.urlConf()
    #浏览器行为
    def getConfUrl(self):
        # self.driver = self.wd
        # self.timeout = 30
        print("open")
        self.wd.get(self.url)
        self.wd.maximize_window()
    def browerClose(self):
        return self.wd.quit()
    def browerSetWindowsSize(self,width,height,windowHandle='current'):
        self.wd.set_window_size(width,height,windowHandle)
    def browerFresh(self):
        self.wd.refresh()
    def browerForward(self):
        self.wd.forward()
    def browerBackward(self):
        self.wd.back()

    #定位
    def findElement(self,*loc):
        #self.wd.find_element(*loc)
        return self.wd.find_element(*loc)

    #元素操作
    def typeText(self,loc,text):
        return  self.wd.find_element(*loc).send_keys(text)
    def clearText(self,*loc):
        return self.wd.find_element(*loc).clear()
    def clickBtn(self,*loc):
        return self.wd.find_element(*loc).click()

    #获取信息行为
    def getWebUrl(self):
        return self.wd.current_url
    def getTitle(self):
        return  self.wd.title
    def checkElementExist(self,*loc):
        flag = True
        try:
            self.findElement(*loc)
        except:
            flag = False
        return flag
    def checkElementDisplayed(self,*loc):
        flag = True
        try:
            self.findElement(*loc).is_displayed()
        except:
            flag = False
        return flag
    @classmethod
    def urlConf(cls):
        cls.host = readconfig.ReadConfig().getserver('host')
        cls.port = readconfig.ReadConfig().getserver('port')
        urlvalue = cls.host + ":" + cls.port
        return urlvalue

if __name__ == '__main__':
    test = BasePage(webdriver.Chrome())
    test.getConfUrl()
   # print(test.getWebUrl())
  #  print(test.getTitle())
    print(test.checkElementDisplayed(By.CLASS_NAME,"error-tip"))
