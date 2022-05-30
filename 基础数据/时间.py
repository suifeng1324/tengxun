# -*- coding uft-8 -*-
# ---
# @Software: PyCharm
# @File: 时间.py
# @Author: yanglei
# @Time: 2022年5月月26日
# ---

import time

# 1. 时间戳    机器看懂时间
# 1970年1月1日 0时0分0秒到现在的偏移量
t = time.time()

# 2. 时间元组   操作时间
print(time.gmtime((t)))  # 0时区
print(time.localtime((t)))  # 本地时区

# 3. 格式化时间 人看懂时间 (2022-05-26 10:58:56)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t)))

# 4. 相互转换  (time.struct_time(tm_year=2022, tm_mon=5, tm_mday=25, tm_hour=10, tm_min=12, tm_sec=44, tm_wday=2, tm_yday=145, tm_isdst=-1)
str_t = '2022-05-25 10:12:44'
print(time.strptime(str_t, "%Y-%m-%d %H:%M:%S"))

# 5. 时间元组转换时间戳  (1653533936.0)
print(time.mktime(time.localtime(t)))

# 6. 时间元组转换为固定化字符 '%a %b %d %H:%S:%Y'  (Thu May 26 10:58:56 2022)
print(time.asctime(time.localtime(t)))
print(time.ctime(t))

# 7. 时间差
t1 = "2022-04-26 11:10:11"
t2 = "2022-04-26 11:41:11"

s1, s2 = time.strptime(t1, "%Y-%m-%d %H:%M:%S"), time.strptime(t2, "%Y-%m-%d %H:%M:%S")  # 转换成元组
a1, a2 = time.mktime(s1), time.mktime(s2)  # 转换成时间戳
diff_time = a2 - a1  # 获取相差秒
print(diff_time)
s_time = time.gmtime(diff_time)
print(time.gmtime(diff_time))
print('过去了{}年{}月{}日{}小时{}分钟{}秒'.format(s_time.tm_year - 1970, s_time.tm_mon - 1, s_time.tm_mday - 1, s_time.tm_hour - 0,
                                       s_time.tm_min - 0, s_time.tm_sec - 0))

# 休眠
# def func():
#     print("你好")
#     time.sleep(5)  # 等待5秒
#     print('这里')


# datatime模块    重新封装了time模块
# date,time,datetime,timedelta,tzinfo
# 1. date
import datetime

# date对象最大，最小日期
print(datetime.date.max)  # 9999-12-31
print(datetime.date.min)  # 0001-01-01
print(datetime.date.today())  # 2022-05-26

# 2.time
# print(datetime.timedelta(0, 0, 1))  # 秒 毫秒 微妙 （0:00:00.000001）
d1 = datetime.datetime(2018, 8, 1, 15, 45, 20)
print(d1)
print(d1 - datetime.timedelta(days=-1))  # 时间差
print(d1 - datetime.timedelta(days=1))  # 时间差

dd = datetime.datetime.now()
d = dd.year  # 获取当前年
d = dd.month  # 获取当前月
d = dd.day  # 获取当前日
d = dd - datetime.timedelta(weeks=1)  # 一周前
d = dd - datetime.timedelta(days=1)  # 一天前
d = dd - datetime.timedelta(hours=1)  # 一小时前
d = dd - datetime.timedelta(minutes=1)  # 一分钟前
d = dd - datetime.timedelta(seconds=1)  # 一秒钟前
