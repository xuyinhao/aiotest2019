from conf import readconfig
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from common.logpy import LogHandler

import sys,os,time
from time import sleep

error_dialog = (By.CLASS_NAME,"dialog-error")
success_dialog = (By.CLASS_NAME,"dialog-success")
waring_dialog = (By.CLASS_NAME,"dialog-warning")
class BasePage():
    '''
    页面的BasePage
    driver : self.wd
    '''
    global logg
    logg = LogHandler().logger

    # def __init__(self,driver=webdriver.Chrome(),url=None):
    def __init__(self,driver,url=None):
        '''
                        初始化 webdriver 并启动
        :param driver:  webdriver.Chrome()
        '''

        self.wd = driver
        # self.wd.implicitly_wait(5)
        self.wd.implicitly_wait(3)
        self.actions = ActionChains(self.wd)
        if url :
            self.url = url
        else:
            self.url = self.server_url_conf()
    #浏览器行为
    def get_conf_url(self):
        '''
        获取配置文件中的测试url
        :return:
        '''
        self.wd.get(self.url)
        self.wd.maximize_window()
        logg.debug("enter conf_url : " + str(self.url))
        try:
            self.wd.find_element_by_id("details-button").click()
            self.wd.find_element_by_id("proceed-link").click()
        except:
            pass
        finally:
            time.sleep(2)
        return  True

    def brower_close(self):
        '''关闭一个窗口'''
        return self.wd.close()
    def brower_quit_all(self):
        '''退出浏览器'''
        return self.wd.quit()
    
    def brower_setwindowssize(self,width,height,windowHandle='current'):
        self.wd.set_window_size(width,height,windowHandle)
        
    def brower_refresh(self):
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

    def submit_func(self,*loc):
        ''' 提交
         loc : (By.ID,"id")
         '''
        return self.wd.find_element(*loc).submit()

    def click_btn(self,*loc):
        '''点击按钮'''
        try:
            self.wd.find_element(*loc).click()
            return True
        except Exception as e:
            logg.error("click_btn error: %s" %(e))
            return False

    # def keyboard_send_f5(self):
    #     loc = (By.CSS_SELECTOR,"[name='log']")
    #     self.find_web_element(*loc).send_keys(Keys.F5)
    
    #鼠标操作
    def mouse_right_click(self,*loc):
        elem = self.find_web_element(*loc)
        self.actions.click(elem).perform(
                                         )
    def mouse_left_click(self,*loc):
        elem = self.find_web_element(*loc)
        self.actions.context_click(elem).perform()
        
    def mouse_double_click(self,*loc):
        elem = self.find_web_element(*loc)
        self.actions.double_click(elem)
        
    def mouse_move_to_element(self,*loc):
        elem = self.find_web_element(*loc)
        self.actions.move_to_element(elem).perform()

    def mouse_drag_and_drop(self):
        pass
    #获取信息行为
    def get_web_url(self):
        return self.wd.current_url
    def get_title(self):
        return  self.wd.title
    def get_element_text(self,*loc):
        return self.find_web_element(*loc).text

    #元素是否存在 是 True
    def check_element_isexist(self,loc):
        '''
        检查元素是否存在
        :param loc:  tuple (By.ID,"id")
        :return: True or False
        '''
        isexist = False
        try:
            EC.presence_of_element_located(loc)(self.wd)
            isexist = True
        except Exception as e:
            isexist = False
            logg.debug(' isexist or not  :',exc_info = True)
        return isexist

    def check_element_has_text(self,loc,text):
        '''
        检查元素文本信息是否存在
        :param loc:  tuple(By.ID,"id")
        :param text: text value
        :return:  True or False
        '''
        try:
            text = EC.text_to_be_present_in_element(loc,text)(self.wd)
        finally:
            return text
    def check_element_isdisplayed(self,*loc):
        flag = True
        try:
            self.find_web_element(*loc).is_displayed()
        except:
            flag = False
        return flag
        # if  EC.visibility_of_element_located(*loc)(self.wd) :
        #     isdisable = True
        # else:
        #     isdisable = False
        # return isdisable
    def __inser_img(self,passorfailed,imgname):
        time_loc = time.strftime("%m%d_%H%M%S",time.localtime())
        file_path = os.path.abspath(__file__)
        file_path = os.path.join(file_path+"/../../log/%s_%s_%s.png" %(passorfailed,imgname,time_loc))
        self.wd.get_screenshot_as_file(file_path)
        logg.debug('Insert— %s_img %s ' %(passorfailed,(file_path)))

    def insert_warning_img(self,imgname):
        sleep(0.5)
        self.__inser_img("waring",imgname)
    def insert_error_img(self,imgname):
        sleep(0.2)
        logg.error(imgname)
        self.__inser_img("error",imgname)
    def insert_success_img(self,imgname):
        sleep(0.2)
        logg.info(imgname)
        self.__inser_img("success",imgname)
    def insert_debug_img(self,imgname):
        sleep(0.2)
        logg.debug(imgname)
        self.__inser_img("debug",imgname)

    def check_dialog_success(self,value):
        if self.check_element_isexist(success_dialog):
            flag = True
            self.insert_success_img(value+"_dialog_success")
        else:
            flag = False
            self.insert_error_img(value+"_dialog_fail")
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
    a = (By.CLASS_NAME, "login-btn")
    test.mouse_move_to_element(*a)
  #   print(test.get_web_url())
  # #  print(test.getTitle())
  #   f_loc = (By.CLASS_NAME,"login-title")
  # #   print(test.check_element_has_text(f_loc,"POPO"))
  #   ff = test.get_element_text(*f_loc)
  #   print(ff)
  #
  #   test.brower_quit_all()
