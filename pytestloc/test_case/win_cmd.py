# -*- coding: CP936 -*-
import pytest
import allure
import subprocess
import time

htmlname = time.strftime("%d%H%M")
allurereporpath="../../log/allurexml"
testcase="test_login_3.py"
# pytest.main(["--rootdir=../../","--html=../../log/report%s.html"%(str(htmlname)),"test_login_3.py"])

def wincmd(cmd):
    a = subprocess.run(cmd,shell=True,stdout=subprocess.PIPE)
    print(a.stdout.decode('cp936'))
    return  a.stdout.decode('cp936')
def genallure_report():
    wincmd('allure generate ./../../log/allurexml/  -o ./../../log/allurexml/report --clean')
def runmain():

    pytest.main(['--reruns','2',"--rootdir=../../",'-q','--alluredir',allurereporpath,testcase])
    genallure_report()
if __name__ == '__main__':
    runmain()
