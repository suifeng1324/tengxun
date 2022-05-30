# author:yangleiw
# createdate:2022/5/18
import time

from selenium.webdriver.common.by import By
from webdriver_helper import *

# 手动关闭浏览器
# driver = get_webdriver()
# driver.get("http://www.baidu.com")
# time.sleep(111)
# driver.quit()

# 控制浏览器
with get_webdriver() as driver:
    driver.get("https://greasyfork.org/zh-CN/users/sign_in?return_to=%2Fzh-CN")
    # 测试动作 + 断言
    time.sleep(1) # 休眠0.5秒
    driver.find_element(By.XPATH, '//input[@id="user_email"]').send_keys("yanglei6408@163.com")
    driver.find_element(By.XPATH, '//input[@id="user_password"]').send_keys("P@ssw0rd123")
    driver.find_element(By.XPATH, '//input[@name="commit"]').click()

    # 获取系统提示
    msg = driver.find_element(By.XPATH, '//p[@class="notice"]').text
    print(msg)
    assert "登录成功" in msg
    # 所有打开的窗口
    # print(driver.window_handles)
    # # 切换窗口，新打开的窗口
    # driver.switch_to.window((driver.window_handles[-1]))
    #
    # #处理弹出
    # driver.switch_to.alert.accept()     #点击确定
    # # 当前窗口
    # print(driver.current_window_handle)
    #
    # driver.find_element(By.XPATH, '//span[text()="货到付款"]').click()



    # driver.find_element(By.ID, "")  # 推荐定位一个元素
    # driver.find_elements(By.ID, "")  # 定位一组元素

    # el = driver.find_element(By.LINK_TEXT, "登录")  # 精确定位
    # el1 = driver.find_element(By.PARTIAL_LINK_TEXT, "登")  # 模糊定位
    # el = driver.find_element(By.ID, "su")  # 精确定位
    # el = driver.find_element(By.NAME, "rsv_spt")  # 精确定位
    # el = driver.find_element(By.CLASS_NAME, "s-top-more-btn")  # 精确定位
    # el = driver.find_element(By.CSS_SELECTOR, ".mnav, c-font-normal, c-color-t")
    # el = driver.find_elements(By.XPATH, '//input[@name="mail"]/../..//input')[0]
    # el.send_keys("12345")

