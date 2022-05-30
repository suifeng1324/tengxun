# author:yangleiw
# createdate:2022/5/19

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _loc_msg = '//p[@class="notice"]'

    def __init__(self, driver: webdriver.Chrome):
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)

    def __getattr__(self, item):
        key = f"_loc_" + item
        xpath = getattr(self, key)

        if xpath:  # 根据xpath进行元素定位
            return self.get_element(xpath)
        raise AttributeError

    def get_element(self, xpath):
        # 元素定位，自动等待
        el = self._wait.until(
            visibility_of_element_located(  # 等待元素出现
                (
                    By.XPATH,
                    xpath,
                )
            )
        )
        return el

    def alert_ok(self):
        alert = self._wait.until(alert_is_present())  # 等待弹窗出现
        alert.accept()  # 点击确定


class LoginPage(BasePage):
    _loc_username = '/html/body/div/div[2]/div[3]/div/div/div/div[2]/div/form/div[1]/div[2]/input'
    _loc_password = '/html/body/div/div[2]/div[3]/div/div/div/div[2]/div/form/div[2]/div[2]/input'
    _loc_submit = '/html/body/div/div[2]/div[3]/div/div/div/div[2]/div/form/div[4]/button'

    def login(self, username, password):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.submit.click()


class AddressPage(BasePage):
    # _loc_new = '//a[text()="收货地址"]'
    _loc_addrs = '/html/body/div[2]/div[1]/div/div/div[3]/div[4]/div/div/textarea'
    _loc_code = '/html/body/div[2]/div[1]/div/div/form/div[1]/div[2]/span/input'
    _loc_name = '/html/body/div[2]/div[1]/div/div/form/div[2]/div[2]/span/input'
    _loc_phone = '/html/body/div[2]/div[1]/div/div/form/div[3]/div[2]/div/div[2]/div/div/span/input'

    def click_new(self):
        pass

    def input_info(self,
                   addrs,
                   code,
                   name,
                   phone):
        self.addrs.sendkeys(addrs)
        self.code.sendkeys(code)
        self.name.sendkeys(name)
        self.phone.sendkeys(phone)
