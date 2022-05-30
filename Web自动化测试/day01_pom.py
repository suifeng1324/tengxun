# author:yangleiw
# createdate:2022/5/18
import time

import pytest
from selenium.webdriver.common.by import By
from webdriver_helper import *

from pages import LoginPage
from pages import AddressPage


@pytest.fixture(scope="session")
def driver():
    driver = get_webdriver()  # 启动浏览器
    driver.delete_all_cookies()  # 清除cookie
    driver.refresh()  # 刷新页面
    driver.maximize_window()  # 窗口最大化
    driver.get("https://greasyfork.org/zh-CN/users/sign_in?return_to=%2Fzh-CN")

    time.sleep(1)  # 休眠0.5秒
    print("测试用例之前")
    # 前置部分，在测试用例之前执行
    yield driver  # 生成器的写法
    # 后置部分，在测试用例之后执行
    print("测试用例之后执行完毕")
    driver.quit()


def test_login_ok(driver):
    # driver.get("https://greasyfork.org/zh-CN/users/sign_in?return_to=%2Fzh-CN")
    # 测试动作 + 断言
    # time.sleep(1)  # 休眠0.5秒

    # 调用page方法，完成交互
    page = LoginPage(driver)
    page.login("yanglei6408@163.com","P@ssw0rd123")

    # driver.find_element(By.XPATH, '//input[@id="user_email"]').send_keys("yanglei6408@163.com")
    # driver.find_element(By.XPATH, '//input[@id="user_password"]').send_keys("P@ssw0rd123")
    # driver.find_element(By.XPATH, '//input[@name="commit"]').click()

    # 获取系统提示
    # msg = driver.find_element(By.XPATH, '//p[@class="notice"]').text
    msg1 = page.msg.text
    print(msg1)
    assert "登录成功" in msg1


def test_login_fail():
    with get_webdriver() as driver:
        # driver.get("https://greasyfork.org/zh-CN/users/sign_in?return_to=%2Fzh-CN")
        # 测试动作 + 断言
        driver.delete_cookie()  # 清除cookie
        driver.refresh()  # 刷新页面
        time.sleep(1)  # 休眠0.5秒
        driver.find_element(By.XPATH, '//input[@id="user_email"]').send_keys("yanglei6408@163.com")
        driver.find_element(By.XPATH, '//input[@id="user_password"]').send_keys("P@ssw0rd123")
        driver.find_element(By.XPATH, '//input[@name="commit"]').click()

        # 获取系统提示
        msg = driver.find_element(By.XPATH, '//p[@class="notice"]').text
        print(msg)
        assert "登录失败" in msg


def test_new_addr(user_driver):
    url1="https://member1.taobao.com/member/fresh/account_security.htm"
    user_driver.get(url1)
    page = AddressPage(user_driver)
    page.click_new() # 点击新增按钮
    page.input_info() # 输入相关内容

    assert "登录失败" in page.msg.text  # 断言