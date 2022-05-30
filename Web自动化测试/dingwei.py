import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):

    def test_01_login(self):
        global driver  # 防止浏览器关闭
        driver = webdriver.Chrome()  # 打开浏览器
        driver.implicitly_wait(10)  # 隐式等待
        driver.get("https://www.126.com")  # 加载网页
        print("/r======Test===========")
        # driver.switch_to.frame('x-URS-iframe1653009354212.643') # 定位子框架（id,name,element)
        driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[contains(@id,"x-URS-iframe")]'))  # 定位子框架（id,name,element)

        driver.find_element(By.XPATH, '//input[@name="email"]').send_keys("yanglei6408@163.com")
        # driver.find_element(By.XPATH, '//input[@id="user_password"]').send_keys("P@ssw0rd123")
        # el = driver.find_element(By.LINK_TEXT, "登录")  # 精确定位
        # el = driver.find_element(By.PARTIAL_LINK_TEXT, "登")  # 模糊定位
        # el = driver.find_element(By.ID, "su")  # 精确定位
        # el = driver.find_element(By.NAME, "rsv_spt")  # 精确定位
        # el = driver.find_element(By.CLASS_NAME, "s-top-more-btn")  # 精确定位
        # el = driver.find_element(By.CSS_SELECTOR, ".mnav, c-font-normal, c-color-t")
        # el = driver.find_elements(By.XPATH, '//input[@name="mail"]') # 相对路径
        # el = driver.find_elements(By.XPATH, '//input[@name="mail" and @id="sr"]') # 相对路径+属性组合

        # el = driver.find_elements(By.XPATH, '//input[@name="mail"]/../..//input')[0]


if __name__ == '__main__':
    unittest.main()
