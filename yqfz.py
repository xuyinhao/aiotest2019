from selenium import webdriver
from common.logpy import LogHandler
from time import sleep
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
import sys
import re
WAIT_TIME = 0.5
#输入项目名
def project_name_input(pro_name):
    wd.find_element_by_id("ctl00_MainContent_txt_Pro").send_keys(pro_name)
    sleep(WAIT_TIME)

#房产公司名称
def business_name_input(business_name):
    wd.find_element_by_id("ctl00_MainContent_txt_Com").send_keys(business_name)
    sleep(WAIT_TIME)

#选择 区域
def domain_name_input(domain_name):
    if domain_name == 1:
        Select(wd.find_element_by_id("ctl00_MainContent_ddl_qy")).select_by_value("RD002")
        sleep(WAIT_TIME)
    elif domain_name == 2:
        Select(wd.find_element_by_id("ctl00_MainContent_ddl_qy")).select_by_value("RD003")
        sleep(WAIT_TIME)
    elif domain_name == 3:
        Select(wd.find_element_by_id("ctl00_MainContent_ddl_qy")).select_by_value("RD004")
        sleep(WAIT_TIME)
    elif domain_name == 4:
        Select(wd.find_element_by_id("ctl00_MainContent_ddl_qy")).select_by_value("RD005")
        sleep(WAIT_TIME)
    elif domain_name == 5:
        Select(wd.find_element_by_id("ctl00_MainContent_ddl_qy")).select_by_value("RD001")
        sleep(WAIT_TIME)
    elif domain_name == 6:
        Select(wd.find_element_by_id("ctl00_MainContent_ddl_qy")).select_by_value("RD008")
        sleep(WAIT_TIME)
    else:
        print("区域选择错误")
        exit(1)

#装修情况 选择
def trim_select(trim_number):
    """
    :param trim_number: 0表示全部，1表示装修房，2表示毛坯
    :return:
    """
    if trim_number == 1:
        wd.find_element_by_id("ctl00_MainContent_rb_HF_CODE_0").click()
        sleep(WAIT_TIME)
    elif trim_number == 2:
        wd.find_element_by_id("ctl00_MainContent_rb_HF_CODE_1").click()
        sleep(WAIT_TIME)
    elif trim_number == 3:
        wd.find_element_by_id("ctl00_MainContent_rb_HF_CODE_2").click()
        sleep(WAIT_TIME)
    else:
        print("装修情况 输入错误")
        exit(1)
#房屋用途选择
def usage_select(usage_num):
    #wd.find_element_by_id("ctl00_MainContent_ddl_houseclass").click()
    if usage_num == 1:
        Select(wd.find_element_by_id("ctl00_MainContent_ddl_houseclass")).select_by_value("1")
        sleep(WAIT_TIME)
    elif usage_num == 2:
        Select(wd.find_element_by_id("ctl00_MainContent_ddl_houseclass")).select_by_value("2")
        sleep(WAIT_TIME)
    elif usage_num == 3:
        Select(wd.find_element_by_id("ctl00_MainContent_ddl_houseclass")).select_by_value("3")
        sleep(WAIT_TIME)
    else:
        print("选择房屋用途失败")
        exit(1)


#输入价格的范围，RMB 单位：元
def price_ange(start_price,end_price):
    wd.find_element_by_id("ctl00_MainContent_txt_Price1").send_keys(start_price)
    sleep(WAIT_TIME)
    wd.find_element_by_id("ctl00_MainContent_txt_Price2").send_keys(end_price)
    sleep(WAIT_TIME)
#属于房屋面积范围
def area_range(start_area,end_area):
    wd.find_element_by_id("ctl00_MainContent_txt_Area1").send_keys(start_area)
    sleep(WAIT_TIME)
    wd.find_element_by_id("ctl00_MainContent_txt_Area2").send_keys(end_area)
    sleep(WAIT_TIME)

#点击查询
def click_search():
    wd.find_element_by_id("ctl00_MainContent_bt_select").click()
    sleep(WAIT_TIME)

def search_info(pj_name,domain,bus_name,trim,price1,price2,area1,area2,usage):
    project_name_input(pj_name)
    domain_name_input(domain)
    business_name_input(bus_name)
    trim_select(trim)
    price_ange(price1,price2)
    area_range(area1,area2)
    usage_select(usage)
    click_search()

def next_page():
    try:
        wd.find_element_by_id("ctl00_MainContent_PageGridView1_ctl22_Next").click()
        sleep(0.2)
    except Exception as e :
        print("next,",e)
    pass
def get_total_page_num(htmlDoc):
    pageNumRe = re.compile(r';--&nbsp;共&nbsp;(.*?)&nbsp;页</td>')
    m = re.findall(pageNumRe,htmlDoc)
    if m is not None: return m


def get_house_other(houseInfoLine):
    sleep(0.01)
    houseNameRe = re.compile(r'false;">(.*?)</td>')
    retHouseName = re.findall(houseNameRe, houseInfoLine)
    houseOtherRe = re.compile(r'<td>(.*?)</td>')
    retHouseOther = re.findall(houseOtherRe,houseInfoLine)
   # print(retHouseOther,retHouseName)
    if retHouseName is None: print("house get name error")
    if retHouseOther is None: print("house get other error")
    try:
        houseName = retHouseName[0]
        houseDes = retHouseOther[0]
        houseSize = retHouseOther[1]
        housePrice = retHouseOther[2]
    except Exception as e:
        print("exception:",e)
    return houseName,houseDes,houseSize,housePrice

def open_excel():
    import win32com.client as win32
    from tkinter import Tk
    global xlBook,xlApp
    excel_value=1
    app = 'excel'
    xlApp = win32.gencache.EnsureDispatch('%s.Application' % app)
    xlApp.Visible = True
    xlBook = xlApp.Workbooks.Add()
def add_sheet(name):
    global shSheet
    xlApp.Worksheets.Add().Name = 'test_house_'+str(name)
    shSheet = xlApp.Worksheets('test_house_'+str(name))

def save_excel(name):
    xlBook.SaveAs(r'e:\excel2.xlsx')
    xlBook.Close(False)
    xlApp.Application.Quit()
def write_info_to_excel(listInfo,num):
    # if not excel_value:
    #     open_excel()
    #     print("open_excel ****")
    shSheet.Cells(1, 1).Value = u'房子位置'
    shSheet.Cells(1, 2).Value = u'房子户型'
    shSheet.Cells(1, 3).Value = u'房子面子'
    shSheet.Cells(1, 4).Value = u'房子单价'
    sleep(0.1)
    # for i in range(1,len(listInfo)):
    shSheet.Cells(num+1, 1).Value = '%s' % str(listInfo[0])
    shSheet.Cells(num+1, 2).Value = '%s' % str(listInfo[1])
    shSheet.Cells(num+1, 3).Value = '%s' % str(listInfo[2])
    shSheet.Cells(num+1, 4).Value = '%s' % str(listInfo[3])
    sleep(0.1)
    # shSheet.Cells(i + 3, 1).Value = "Th-th-th-that's all folks!"
    # sleep(4)
    # xlBook.SaveAs(r'excel_house.xlsx')
    # xlBook.Close(False)
    #
    # xlApp.Application.Quit()

if __name__ == '__main__':
    open_excel()
  #  nameList=["怡邻","青灯","淞泽","阳澄","悬珠","新娄花园","亭苑","厦亭","青苑","滨江苑"]
    nameList=["青剑湖","莲香新村","荷韵新村","古娄","畅苑"]
    add_sheet("ttt2")
    num = 0
    for xqname in nameList:
        wd = webdriver.Chrome()
        #打开浏览器页面并登录网站
        wd.get("http://spf.szfcweb.com/szfcweb/(S(ss4uoi452xbjmujqlgf41y45))/DataSerach/CanSaleHouseSelectIndex.aspx")
        #项目名称：pj_name； 区域：1~6：1园区，2吴中，3相城，4高新，5姑苏，6吴江
        pj_name=xqname ; domain=1
        #房产公司名称：bus_name ; 装修情况 1全部， 2 装修 3毛坯
        bus_name="";trim=1
        #房屋价格price1,price2 ; 房屋面积： area1,area2
        price1,price2="",""; area1,area2="",""
        #房屋用途 1住宅 ，2非住宅， 3 其他
        usage_num=1

        # add_sheet(pj_name)
        search_info(pj_name,domain,bus_name,trim,price1,price2,area1,area2,usage_num)
        html = wd.execute_script("return document.documentElement.outerHTML")

        # for i in html:
        if "共&nbsp;" in html:
            totalNum = get_total_page_num(html)
            print(totalNum[0])


        for j in range(0, int(totalNum[0])):
            html = wd.execute_script("return document.documentElement.outerHTML")
            f = open("html1", "w", encoding="utf8")
            f.write(html) ; f.close()

            with open("html1",encoding="utf8") as f:
                for i in f:
                    if "<td onmouseover=\"c=this.style.backgroundColor" in i:
                        if "onmouseout" in i:
                            ret = get_house_other(i)
                            print(ret)
                            num += 1
                            write_info_to_excel(ret,num)
            if j < int(totalNum[0])-1:
                next_page()
                sleep(0.1)
                # if "<td onmouseover=\"c=this.style.backgroundColor" in i :
                #     if "onmouseout" in i:
                #         ret = get_house_other(i)
                #         print(ret)
        print(num)
    save_excel(r"e:\ex2.xlsx")



