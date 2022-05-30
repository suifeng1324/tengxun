# author:yangleiw
# createdate:2022/5/20

import requests

url = "http://api.tianapi.com/caipu/index"
# headers = {'Content-type': 'application/x-www-form-urlencoded'}
data = {
    "key": "52102c578161830ebd6496f76c1cfde9",
    "word": "黄瓜",
    "num": 10,
    "page": 1

}
# req = requests.get(url, params=data)
# print(req.json())
# 发送post请求（data和json只需传一个）
# req = requests.post(url, json=json.dumps(data))
req = requests.post(url, data=data)
print(req.json())
print(req.json()['newslist'][0]['type_name'])

# rep = requests.request()

# print(rep.text)  # 返回字符串的数据
# print(rep.content)  # 返回字节格式的数据
# print(rep.json())  # 返回字典格式的数据
# print(rep.status_code)  # 返回字状态码
# print(rep.reason)  # 返回状态信息
# print(rep.cookies)  # 返回cookie信息
# print(rep.encoding)  # 返回编码格式
# print(rep.headers)  # 返回响应头信息
