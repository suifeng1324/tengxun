# author:yangleiw
# createdate:2022/5/17

import base64
import json

from Crypto.Cipher import AES

# 在这里定义好加密和解密代码
# 让测试用例直接调用即可

# AES加密
key = b"sanmu's aes_key!"  # 16为字节作为密钥
mode = AES.MODE_EAX
IV = b"0" * 16
encoder = AES.new(key, mode, nonce=IV)


class Encoder:
    # @staticmethod
    def encrypt(self, data: dict) -> str:
        """
        AES数据加密
        1. 接受字典
        2. 字典转字符串
        3. 字符串转字节
        4. 字节进行加密
        5. 对加密结果进行base64
        6. 编码结果进行字符串
        :param data:
        :return:
        """
        content_str = json.dumps(data)
        content_en, b = encoder.encrypt_and_digest(content_str.encode("utf-8"))  # 将字符串转二进制字节流
        return base64.b64encode(content_en).decode("utf-8")

    @staticmethod
    def decrypt(data: str) -> dict:
        """
        AES数据解密
        1. 接受字符串
        2. 字符串转字节
        3. base64解码
        4. AES解密
        5. 解密结果转字符串
        6. 字符串转字典
        :param data:
        :return:
        """
        encoder = AES.new(key, AES.MODE_EAX, nonce=IV)

        content_byte = base64.b64decode(data)
        content_de = encoder.decrypt(content_byte)
        content_str = content_de.decode("utf-8")  # 将字符串转二进制字节流
        content = json.loads(content_str)
        return content

    def __init__(self):
        print("调用libs2")
# data = """
# {
#     "username": "sanmu",
#     "password": "123456"
# }
# """

# # 元组解包
# a, b = encoder.encrypt_and_digest(data.encode("utf-8"))  # 将字符串转二进制字节流
# print(a)
# print(base64.b64encode(a))  # base64 加密结果
# print(base64.b64encode(a).decode("utf-8"))  # 加密结果转字符串
# print("=============")
# print(b)
# print(base64.b64encode(b))  # base64 加密结果
# print(base64.b64encode(b).decode("utf-8"))  # 加密结果转字符串
