from selenium import webdriver
import os

#截图
def insert_img(driver,file_name):
    file_path ="../report/image/"+file_name
    driver.get_screenshot_as_file(file_path)
    return

if __name__ == '__main__':
    driver=webdriver.Chrome()
    driver.get('https://www.baidu.com')
    insert_img(driver,'baidu.png')
    driver.quit()
