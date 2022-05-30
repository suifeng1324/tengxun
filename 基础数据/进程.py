# -*- coding uft-8 -*-
# ---
# @Software: PyCharm
# @File: 进程.py
# @Author: yanglei
# @Time: 2022年5月月29日
# ---

# 多任务介绍
import multiprocessing
import os
import time


def func1():
    # 获取当前进程的编号,父进程编号
    print("funct1:", os.getpid(), os.getppid())


def func2():
    print("funct2:", os.getpid(), os.getppid())
    time.sleep(1)
    print("funct2:", os.getpid(), os.getppid())


if __name__ == '__main__':
    print(os.getpid())
    # 创建子进程
    process1 = multiprocessing.Process(target=func1)
    process2 = multiprocessing.Process(target=func2)

    # 启动子进程执行任务
    process2.start()
    process1.start()
