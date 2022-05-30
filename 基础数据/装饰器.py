# -*- coding uft-8 -*-
# ---
# @Software: PyCharm
# @File: 装饰器.py
# @Author: yanglei
# @Time: 2022年5月月26日
# ---

# 定义  装
# def demo():
#     print('hello')

# 调用 取
# demo()
import time


def outer(flag):
    def timer(func):  # 装饰函数
        def inner():  # 闭包函数
            if flag:
                start = time.time()
            re = func()
            if flag:
                print(time.time() - start)
            return re

        return inner

    return timer


# @timer  # 语法糖 func2 = timer(func2)
@outer(True)
def func2():
    print('in func2')
    time.sleep(3)


# func2 = timer(func2)  # 地址的改变
func2()  # inner()
