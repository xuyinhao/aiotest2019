
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.baidu.com")
        self.assertIn("百度一下", driver.title)
        elem = driver.find_element_by_id("kw")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        sleep(1)
        assert "pycon" in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
