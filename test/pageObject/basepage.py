#PageObject（页面对象），
# 简单点说就是把界面定位和业务操作分开。
# 这个框架主要是把UI自动化分为三层：对象库层、操作层和业务层。
from selenium import webdriver
from common.browser import browser
from common.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time  import sleep
class BaiduPage(BasePage):
    url='https://www.baidu.com'
    tkw=(By.ID,'kw')
    def __init__(self,selenium_driver,base_url="",parent=None):
        self.base_url=base_url
        self.driver=selenium_driver
        #self.driver=webdriver.Chrome()
        self.timeout = 30
        self.parent=parent
        self.searchid='kw'
    def _open(self,url):
        url=self.base_url+url
        self.driver.get(url)
       # assert self.on_page(),'aaa'
    def open(self):
        self._open(self.url)
    def find_element(self,*loc):
        return 1
    def search(self,searchcontent):
       # self.driver.find_element_by_id(self.searchid).send_keys(searchcontent)
        searchtext=self.driver.find_element(*BaiduPage.tkw)
        searchtext.send_keys(searchcontent)
    def clear(self):
        clr=self.driver.find_element(*BaiduPage.tkw)
        clr.clear()
    def click_bdyx(self):
        self.driver.find_element_by_id('su').click()
if __name__ == '__main__':
    driver=browser()
    aa=BaiduPage(driver)
    aa.open()
    aa.search('wd')
    aa.click_bdyx()
    sleep(2)
    driver.quit()

