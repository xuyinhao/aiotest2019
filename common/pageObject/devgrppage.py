from selenium import webdriver
from common.base_page import BasePage
from common.logpy import LogHandler
from common.pageObject.homepageobj import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import time,sys
from conf import readconfig

class DevgrpPage(HomePage):
    global logg
    logg = LogHandler().getlog()
    store_menu = (By.CSS_SELECTOR,"div.menu-content[data-title='云存储']")
    devgrp_menu = (By.CSS_SELECTOR,"div.menu-content[data-title='设备分组管理']")
    check_default = (By.CSS_SELECTOR,"td.has-split[title='default']")
    create_devgrp_loc = (By.NAME,"create-group")
    input_devgrp_name_loc = (By.CSS_SELECTOR,".mb-body >form:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)")
    input_devgrp_name_confirm = (By.CLASS_NAME,"custom-button")
    bind_dev = (By.NAME,"bind-device")
    add_dev_bynode = (By.NAME,"byNode")
    add_dev_byid = (By.NAME,"byId")
    limit_switch = (By.CLASS_NAME,"loong-switch-open")
    error_dialog = (By.CLASS_NAME,"dialog-error")
    success_dialog = (By.CLASS_NAME,"dialog-success")
    waring_dialog = (By.CLASS_NAME,"dialog-warning")
    add_dev_input_ip = (By.CLASS_NAME,"loong-search-input")
    add_dev_select_ip = (By.CSS_SELECTOR,"li.option:first-child")
    dev_list_add_submit = (By.CLASS_NAME,"custom-button")
    check_bynode_devlist = (By.CSS_SELECTOR,"td[title^='/dev']")
    bynode_devlist_firstdev =(By.CSS_SELECTOR,"td[style='padding-left: 10px;']")
    #按照firstdev 获取同级哥哥节点 来拿到 DevID
    get_bynode_devlist_firstdevID = (By.XPATH,"//td[starts-with(@title,'/dev')]/preceding-sibling::td[1]")
    def dev_list_elems(self,num):
        self.dev_list = (By.CSS_SELECTOR,"tr[data-index]:nth-child(%d)"%(num))
    #devgrp_name_click = By.CSS_SELECTOR,"td.has-split[title="+groupname+"]"

    def init_web(self):
        flag =True
        self.correct_login()
        self.click_devgrp_manager_menu()
        logg.info("devgroup wait 3s")
        sleep(3)
        # self.click_btn(*self.check_default)
        if not self.check_groupname_result("default"):
            logg.error('initweb check default grp : error' )
            flag = False
        return  flag
            # self.brower_close()

    def create_devgrp(self,devgrpname):
        flag = True

        if self.check_groupname_result(devgrpname):
            logg.warn('Dev group %s already exist' % devgrpname)
            return False

        self.click_btn(*self.create_devgrp_loc)
        self.type_text(self.input_devgrp_name_loc,devgrpname)
        self.click_btn(*self.input_devgrp_name_confirm)
        logg.debug(print(*self.input_devgrp_name_confirm))

        if not self.check_groupname_result(devgrpname):
            self.insert_error_img('** check %s grp : error ' %(devgrpname))
            flag = False
        sleep(2)
        return flag

    def click_devgroup_name(self,groupname):
        try:
            self.click_btn(By.CSS_SELECTOR,"td.has-split[title="+groupname+"]")
            sleep(0.4)
            return True
        except Exception as e:
            logg.error('%s error ： %s'%(sys._getframe().f_code.co_name,e))
            return False

    def _get_firstdevID(self):
        value = self.get_element_text(*self.get_bynode_devlist_firstdevID)
        logg.info("firstdevID : %s "%(value))
        return value

    def check_dialog_error(self):
        if self.check_element_isexist(self.error_dialog):
            flag =True
            self.insert_success_img("devgrp_dialog_error")
        else:
            flag = False
            self.insert_error_img("devgrp_dialog_error")
        sleeptime = 5
        logg.info("** dialog   check_dialog_error sleep %ss...  "%(sleeptime))
        sleep(sleeptime)
        return flag

    def check_dialog_warning(self,content=None):
        if self.check_element_isexist(self.waring_dialog):
            flag =True
            self.insert_success_img("devgrp_dialog_warning_%s"%(content))
        else:
            flag = False
            self.insert_error_img("devgrp_dialog_warning_%s"%(content))
        sleeptime = 5
        logg.info("** dialog check_dialog_warning sleep %ss...  "%(sleeptime))
        sleep(sleeptime)
        return flag

    def check_dialog_success(self):
        if self.check_element_isexist(self.success_dialog):
            flag = True
            self.insert_success_img("devgrp_dialog_success")
        else:
            flag = False
            self.insert_error_img("devgrp_dialog_fail")
        # sleeptime = 5
        # logg.info("** dialog check_dialog_success sleep %ss...  "%(sleeptime))
        # sleep(sleeptime)
        return flag

    def move_to_add_dev(self):
        self.mouse_move_to_element(*self.bind_dev)

    def add_dev_by_node_noclick_devgrp(self):
        ''' 不主动选择设备分组，直接添加 bynode'''
        self.move_to_add_dev()
        self.click_btn(*self.add_dev_bynode)
        sleep(0.5)
        if not self.check_dialog_warning("add_dev_by_node_noclick_devgrp"):
            logg.error("add_dev_by_node_noclick_devgrp error")
            return False
        logg.debug("add_dev_by_node_noclick_devgrp pass")
        return True

    def add_dev_by_id_noclick_devgrp(self):
        ''' 不主动选择设备分组，直接添加 byid'''
        self.move_to_add_dev()
        self.click_btn(*self.add_dev_byid)
        sleep(0.5)
        if not self.check_dialog_warning():
            logg.error("add_dev_by_devid_noclick_devgrp error")
            return False
        logg.debug("add_dev_by_devid_noclick_devgrp pass")
        return True

    def check_searchbynodeip_devlist_result(self):
        #搜索ip后，应该会展示有 /dev
        try:
            c = self.check_element_isexist(self.check_bynode_devlist)
            return True
        except Exception as e:
            logg.error("check_searchbynodeip_devlist_result error : %s"%(e))
            return False

    def enter_node_ip_and_click(self,nodeip):
        self.type_text(self.add_dev_input_ip,nodeip)
        if self.click_btn(*self.add_dev_select_ip):
            logg.info("enter_node_ip_and_click okkkk")
        else:
            logg.error("enter_node_ip_and_click error ")
            return False
        waittime = 5
        logg.info("wait enter_node_ip_and_click %ss " %(waittime))
        sleep(waittime)
        if self.check_searchbynodeip_devlist_result():
            return True
        else:
            return False

    def select_firstonedevice_from_nodeipdevlist(self):
        if self.click_btn(*self.bynode_devlist_firstdev):
            #获取一下当时的devID
            value = self._get_firstdevID()
            with open('.tmp','w') as f:
                f.write(value)
                f.close()
            self.click_btn(*self.dev_list_add_submit)
        sleep(2)
        if self.check_dialog_success():
            logg.info("select_firstonedevice_from_nodeipdevlist check ok")
            return True
        else:
            logg.error("check_dialog_success error")
            return False

    def add_dev_by_nodeip(self):
        self.move_to_add_dev()
        if self.click_btn(*self.add_dev_bynode):
            sleep(0.5)
            logg.info("通过nodeip增加设备 成功")
            return True
        else:
            self.insert_error_img("通过nodeip增加设备 失败")
            return False

    def add_dev_to_devgrp_by_nodeip(self,devgrpname,nodeip):
        """仅仅添加第一个设备到devgrpname"""
        sleep(1)
        if self.click_devgroup_name(devgrpname):
            if self.add_dev_by_nodeip():
                if self.enter_node_ip_and_click(nodeip):
                    if self.select_firstonedevice_from_nodeipdevlist():
                        logg.info("select_firstonedevice_from_nodeipdevlist pass")
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

        pass

    def add_dev_to_devgrp_by_deviceid(self):
        pass

    def delete_devgrp_noclickfirst_devgrp(self):
        ''' 不主动选择设备分组，直接删除 '''
        pass

    def delete_devgrp_by_select_devgrp(self):
        pass

    def check_limit_switch(self):
        pass
    def open_limit_switch(self):
        pass

    def close_limit_switch(self):
        pass

    def set_devgrp_limit(self):
        pass


    def check_groupname_result(self,groupname):
        flag = False
        if self.check_element_isexist((By.CSS_SELECTOR,"td.has-split[title="+groupname+"]")):
            flag = True
        logg.info("%s group exist is : %s" %(groupname,str(flag)))
        return  flag

if __name__ == '__main__':
    test = DevgrpPage(webdriver.Chrome())
    test.init_web()
    test.create_devgrp("dev12")
    # if test.click_devgroup_name("dev12"):
    #     test.add_dev_by_node_noclick_devgrp()
   #支持按照ip为分组添加设备（默认是第一个dev）
    print(test.add_dev_to_devgrp_by_nodeip("dev12","13.10.12.30"))



    #
    # test.mouse_move_to_element(By.NAME,"bind-device")
    # test.click_btn(By.NAME,"byNode")
    # for i in range(11,12):
    #     name = "dev"+str(i)
    #     ret = test.create_devgrp(name)
    #     if ret :
    #         logg.info(name + " : pass")
    #     else:
    #         logg.error(name + " : error")

