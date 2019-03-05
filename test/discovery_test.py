from common.browser import browser
import unittest
import os
test_dir = 'testcase'
#定义要执行的测试用例的路径和名称格式
#test_*.py的意思是，./testcase路径下文件名称格式为test_*.py的文件，*为任意匹配，路径下有多少的test_*.py格式的文件，就依次执行几个
# discover=[None]*50
discover=[]
aa=['login','write','test']
for i in aa:
    discover.append(unittest.defaultTestLoader.discover(test_dir, pattern=str(i)+"*"))

print(discover)

