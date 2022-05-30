# -*- coding uft-8 -*-
# ---
# @Software: PyCharm
# @File: 文件.py
# @Author: yanglei
# @Time: 5月 24,2022
# ---
import os

"""
with open() as f
    f.write()
    f.read()
"""

# f = open(r'C:\Users\admin\Desktop\1.txt', mode='w', encoding='utf-8')

# 读取文本
# print(f.read())
# print(f.readline())
# print(f.readlines())

# 写入文本
# f.write('make')
# f.writelines(['make', 'nake'])

# 指针
# 起始位置 0 文件开头 1 当前位置 2 文件末尾
# f.seek(0, 1)
# f.write("0")
#
# 关闭
# f.close()

# ==============================================================
# 文件备份
# ==============================================================
# old_name = input("输入备份文件名：")
# index = old_name.rfind('.')
# new_name = old_name[:index] + '[备份]' + old_name[index:]
#
# old_f = open(old_name, 'rb')
# new_f = open(new_name, 'wb')
#
# while True:
#     con = old_f.read(1024)
#     if len(con) == 0:
#         break
#     new_f.write(con)
#
# old_f.close()
# new_f.close()
# ==============================================================
# 文件和文件夹操作
# ==============================================================

# 重命名
# os.rename(r"C:\Users\admin\Desktop\1.txt",r'C:\Users\admin\Desktop\2.txt')

# 删除
# os.remove(r'C:\Users\admin\Desktop\1.txt')

# 创建文件夹
# os.mkdir(r'C:\Users\admin\Desktop\python')

# 获取当前目录
# print(os.getcwd())

# 删除文件夹
# os.rmdir(r'C:\Users\admin\Desktop\python')

# 改变默认目录
# os.chdir(r'C:\Users\admin\Desktop\python)

# 拼接路径=当前目录下文件
print(os.path.join(os.getcwd(), '文件.txt'))

