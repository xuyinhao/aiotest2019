from selenium import webdriver
from common.base_page import BasePage
from common.logpy import LogHandler
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from conf import readconfig
from common.pageObject.aiologinpage import AioLogin
from data.get_data import GetData
from common.pageObject.devgrppage import DevgrpPage

gd = GetData()


# 登录页面检查
# o = BasePage()
# o.get_conf_url()


# for row in [2,3,4]:
#     element = gd.get_elements_by_and_key(row)
#     # print(type(element))
#     m=o.check_element_isexist(element)
#     try:
#         if m :
#             gd.write_current_result(row,'pass')
#         else:
#             gd.write_current_result(row, 'fail')
#     except Exception as e:
#         gd.write_current_result(row, 'fail : ' + str(e))
#
# print('test end')
# o.brower_close()


# 主页面 按钮检查
# ai = AioLogin()
# ai.correct_login()
# for row in range(5,19):
#     element = gd.get_elements_by_and_key(row)
#     # print(type(element))
#     m=ai.check_element_isexist(element)
#     try:
#         if m :
#             gd.write_current_result(row,'pass')
#         else:
#             gd.write_current_result(row, 'fail')
#     except Exception as e:
#         gd.write_current_result(row, 'fail : ' + str(e))
#
# ai.brower_close()

def _check_and_write_result(m):
    try:
        if m:
            gd.write_current_result(row, 'pass')
        else:
            gd.write_current_result(row, 'fail')
    except Exception as e:
        gd.write_current_result(row, 'fail : ' + str(e))


# 设备分组页面检查
dg = DevgrpPage()
dg.init_web()
for row in range(18, 23):
    element = gd.get_elements_by_and_key(row)
    # print(type(element))
    dp_method = gd.get_dependent_method(row)
    get_ele = gd.get_elements_by_dependent_row(row)
    if dp_method == "click":
        fw = dg.find_web_element(*get_ele).click()
        m = dg.check_element_isexist(element)
        _check_and_write_result(m)
        # 先要处理一下
        dg.init_web()
        continue
    if dp_method == "move":
        dg.mouse_move_to_element(*get_ele)
        m = dg.check_element_isexist(element)
        _check_and_write_result(m)
        # 先要处理一下
        dg.init_web()
        continue

    m = dg.check_element_isexist(element)
    _check_and_write_result(m)

dg.brower_close()
