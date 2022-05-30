# author:yangleiw
# createdate:2022/5/19
import time
import unittest

from selenium import webdriver


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test01_login(self):
        global driver  # 防止浏览器关闭
        driver = webdriver.Chrome()
        driver.get("https://www.tianapi.com/login.html")
        time.sleep(3)
        driver.add_cookie({"name": "Hm_lvt_b37eeb8191b3cc8b1e5ed80bd1406aac", "value": "1652973598"})
        driver.add_cookie({"name": "Hm_lpvt_b37eeb8191b3cc8b1e5ed80bd1406aac", "value": "1652973598"})
        driver.add_cookie({"name": "uusid", "value": "aia4nsp1589frnq2etk3uso56t"})
        driver.add_cookie({"name": "acw_tc", "value": "76b20f6416529735980775278e06cc039ef33e4486693e0f21693234e89215"})
        time.sleep(3)
        driver.get("https://www.tianapi.com/console/")
        # cks = driver.get_cookies()
        # for ck in cks:
        #     print(ck)
        # time.sleep(20)
        # # 手动登录一次
        # for ck in cks:
        #     print(ck)

    # {'domain': '.tianapi.com', 'expiry': 1684509597, 'httpOnly': False,
    #  'name': 'Hm_lvt_b37eeb8191b3cc8b1e5ed80bd1406aac', 'path': '/', 'secure': False, 'value': '1652973598'}
    # {'domain': '.tianapi.com', 'httpOnly': False, 'name': 'Hm_lpvt_b37eeb8191b3cc8b1e5ed80bd1406aac', 'path': '/',
    #  'secure': False, 'value': '1652973598'}
    # {'domain': 'www.tianapi.com', 'expiry': 1653232797, 'httpOnly': False, 'name': 'uusid', 'path': '/',
    #  'secure': False, 'value': 'aia4nsp1589frnq2etk3uso56t'}
    # {'domain': 'www.tianapi.com', 'expiry': 1652975397, 'httpOnly': True, 'name': 'acw_tc', 'path': '/',
    #  'secure': False, 'value': '76b20f6416529735980775278e06cc039ef33e4486693e0f21693234e89215'}
    # {'domain': '.tianapi.com', 'expiry': 1684509597, 'httpOnly': False,
    #  'name': 'Hm_lvt_b37eeb8191b3cc8b1e5ed80bd1406aac', 'path': '/', 'secure': False, 'value': '1652973598'}
    # {'domain': '.tianapi.com', 'httpOnly': False, 'name': 'Hm_lpvt_b37eeb8191b3cc8b1e5ed80bd1406aac', 'path': '/',
    #  'secure': False, 'value': '1652973598'}
    # {'domain': 'www.tianapi.com', 'expiry': 1653232797, 'httpOnly': False, 'name': 'uusid', 'path': '/',
    #  'secure': False, 'value': 'aia4nsp1589frnq2etk3uso56t'}
    # {'domain': 'www.tianapi.com', 'expiry': 1652975397, 'httpOnly': True, 'name': 'acw_tc', 'path': '/',
    #  'secure': False, 'value': '76b20f6416529735980775278e06cc039ef33e4486693e0f21693234e89215'}

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
