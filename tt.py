# author:yangleiw
# createdate:2022/5/19
import unittest

from selenium import webdriver


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test01_login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.tianapi.com/login.html")
        cks = driver.get_cookies()
        for ck in cks:
            print(ck)

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()