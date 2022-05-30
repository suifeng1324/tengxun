# -*- coding uft-8 -*-
# ---
# @Software: PyCharm
# @File: 正则表达式.py
# @Author: yanglei
# @Time: 2022年5月月26日
# ---
import re

# 正则表达式

# 匹配单个字符
# \d 匹配数字
# \D 匹配非数字

# 匹配多个字符
# \d+
# \d{11}
# \d{11,12}

# re模块

# finall() 匹配所有符合规则的内容
# 匹配中文
str = "hello 你好333啊 json是的"
res = re.findall('([\u4e00-\u9fa5]+)', str)
print(res)

# match() 只能匹配字符串的开头
result = re.match('\d', '9hello2')
print(result.group())  # 匹配结果需要group导出

# search() 只能匹配一次，返回第一次匹配结果
result = re.search('\d', '9hello9')
print(result.group())  # 匹配结果需要group导出

# compile() 编译正则表达式对象
res = re.compile('\d')
result = re.findall(res, 'hello9word')

# split() 匹配完成后分割
result = re.split('@', '417752356@qq.com')[0]
print(result)

# sub() 替换
result = re.sub('@qq', '@163', '417752356@qq.com')
print(result)
