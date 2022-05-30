# author:yangleiw
# createdate:2022/5/17

import requests

from libs2 import Encoder

login_info = {
    'username': 'sanmu',
    'password': '123456'
}

_data = {
    "content": Encoder().encrypt(login_info),  # 内容使用AES加密,一定是字符串
    "cipher": "AES"
}

resp = requests.post('https://api.tttt.one/rest-v1/encrypt/with_json', json=_data)

assert resp.status_code == 200, resp.json()  # 数据加密正确，请求成功
# assert resp.json() == {
#     "content": "string",
#     "cipher": "AES"
# }
# 验证数据的格式，而不是值
assert "content" in resp.json()
assert "cipher" in resp.json()
print(resp.json())

# 验证数据的值
# 解密 resp.json()['content']
resp_data = Encoder.decrypt(resp.json()['content'])
print(resp_data)  # 解密后的数据
assert "token" in resp_data
# 测试通过
