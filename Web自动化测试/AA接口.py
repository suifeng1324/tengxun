import time

import json
import requests

re = requests.session()
# 10.202.64.51 为要修改的ip
url = 'https://xxxxx/v1/authentication'
url1 = 'https://xxxxx/v3/automations/deploy'
url2 = 'https://xxxxx/v2/activity/list'

# username 为登录的用户名
# password 为登录的密码
data = {
    'username': 'xxxx',
    'password': 'xxxxx'
}
data = json.dumps(data)

r = re.post(url, data=data, verify=False)

print(r.json)
print('-----------------------------------------------')

dict1 = r.json()
print(dict1)
token = dict1['token']
# fileId 为要启动的Maintask的ID
# runAsUserIds 为当前登录账号的userID userID用admin账号登录查看
# poolIds 为连接池的ID
body = {
    'fileId': '33',
    "runAsUserIds": [8],
    "poolIds": [1],
    'overrideDefaultDevice': False,
    "automationName": "bot01-下载核对文件",
}
body = json.dumps(body)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',
    'X-Authorization': token
}
r = re.post(url1, data=body, json=data, headers=headers, verify=False)
print(r.json)
print(r.json())
print('-----------------------------------------------')

# operator 为登录的用户名
body = {
    "filter": {
        "operator": "xxxxx",
        "field": "deploymentId",
        "value": r.json()['deploymentId']
    }
}
body = json.dumps(body)
time.sleep(5)
r = re.post(url2, data=body, json=data, headers=headers, verify=False)

print(r.json)
with open("data.txt", "w") as f:
    f.write(r.text)

print('-----------------------------------------------')

r.close()
re.close()
del re
del r
# input()
