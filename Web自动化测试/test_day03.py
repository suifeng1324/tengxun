# author:yangleiw
# createdate:2022/5/19
import pytest
from webdriver_helper import *

from pages import *


@pytest.fixture(scope="session")
def user_driver():
    driver = get_webdriver()
    driver.maximize_window()
    driver.get("https://member1.taobao.com/member/fresh/deliver_address.htm?spm=a1z08.2.0.0.2167978bM3gjOx")
    login_page=LoginPage(driver)
    login_page.login("suifeng1324","YANGlei1324")
    # 完成了登录

    yield driver
    driver.quit()


@pytest.mark.parametrize("addrs,code,name,phone", [
    ["南昌", "330002", "杨磊", "17607091936"],
])
def test_new_address(user_driver, addrs, code, name, phone):
    page = AddressPage(user_driver)
    page.input_info(
        addrs,
        code,
        name,
        phone,
    )


@pytest.mark.parametrize(
    "i",  # 参数名
    range(2),  # 参数名

)
def test_b(i):  # 有参数
    print(f"这是{i}个测试用例")
