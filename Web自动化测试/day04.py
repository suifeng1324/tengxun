# author:yangleiw
# createdate:2022/5/19
import unittest
from selenium.webdriver.common.by import By
from webdriver_helper import *


class TestCase(unittest.TestCase):

    def test_01_login(self):
        # 打开浏览器
        driver = webdriver_helper.Chrome()
        # 加载网页
        driver.get("http://www.baidu.com")
        el = driver.find_element(By.XPATH, '//a[text()="图片"]')
        print(el)
