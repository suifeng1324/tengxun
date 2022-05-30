"""
@Author :       yangleiw
@File   :       .py
@Time   :       2022年05月22日 10:24
@Desc   :
"""

import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

global driver
url = "http://www.taobao.com"
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # 隐式等待
driver.get(url)
driver.maximize_window()


def get_product():
    # 登录
    # driver.find_element(By.XPATH, '//input[@id="fm-login-id"]').send_keys("suifeng1324")
    # driver.find_element(By.XPATH, '//input[@id="fm-login-password"]').send_keys("YANGlei1324")
    # driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    lists = driver.find_elements(By.XPATH, '//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    with open(r"book.csv", "a", encoding='utf-8') as f:
        for li in lists:
            price = li.find_element(By.XPATH, './/div[@class="price g_price g_price-highlight"]/strong').text
            src = li.find_element(By.XPATH, './/a[@class="J_ClickStat"]').get_attribute('href')
            info = li.find_element(By.XPATH, './/a[@class="J_ClickStat"]').text
            f.write("{},{},{}\n".format(info, price, src))
    # if __name__ == "__main__":
    #     pass


def search():
    driver.find_element(By.ID, "q").send_keys("python")
    driver.find_element(By.CLASS_NAME, "btn-search").click()
    time.sleep(10)
    res = driver.find_element(By.XPATH, '//div[@class="total"]').text
    pages = re.findall("(\d+)", res, re.S)
    return int(pages[0])


def drop_down():  # 滑动鼠标
    for x in range(1, 11, 2):
        time.sleep(0.5)
        j = x / 10  # 滑动到的位置
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)


def next_page():  # 点击下一页
    page = search()
    num = 0
    while num != page - 1:
        driver.get("https://s.taobao.com/search?q={}&s={}".format(keyword, 44 * num))
        driver.implicitly_wait(10)  # 隐式等待
        num += 1
        drop_down()
        get_product()


if __name__ == '__main__':
    keyword = "python"
    next_page()

# 实例图形化
# root = tk.Tk()
# root.geometry("500x220")
# root.title("杨磊制作淘宝查询")
# lable1 = tk.Label(root, text='查询物品：')
# lable1.grid(row=4, column=0)
#
# text1 = tk.Entry(root, text="", width=50)
# text1.grid(row=4, column=1)
#
#
# def cx():  # 播放
#     get_product(text1.get())
#
#
# button1 = tk.Button(root, text="查询", width=8, command=cx)
# button1.grid(row=5, column=1)
#
#
# def qc():  # 清除
#     text1.delete(0, "end")
#
#
# button2 = tk.Button(root, text="清除", width=8, command=qc)
# button2.grid(row=6, column=1)
#
# # button2 = tk.Button(root, text="",width=8)
# # button2.grid(row=5, column=1)
#
# # 菜单
# menubar = tk.Menu(root)  # 实例化菜单
# helpmenu = tk.Menu(menubar, tearoff=0)  # 在菜单上生成子菜单
# menubar.add_cascade(label='帮助(H)', menu=helpmenu)  # 增加一个主菜单选项
#
#
# def helpmsg():
#     print("hello")
#
#
# helpmenu.add_command(label='帮助文档', command=helpmsg)
# helpmenu.add_command(label='作者信息')
# root.config(menu=menubar)
#
# root.mainloop()  # 一直刷新窗口，否则一开就关闭了
