"""
@Author :       yangleiw
@File   :       .py
@Time   :       2022年05月22日 14:37
@Desc   :
"""
from aip import AipOcr
from aip import AipSpeech

# 文字识别
""" 你的 APPID AK SK """
APP_ID = '26288727'
API_KEY = 'wPXXMe6WY3ERKmSc72U6q6kw'
SECRET_KEY = 'yZGUNhiP2j3wLZuI7ZbrIobyRDLt1y3P '

""" 读取文件 """
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
filePath = r'D:\PycharmProjects\tengxun\python_project_demo\百度'


def get_file_content(filePath):
    with open(filePath, "rb") as fp:
        return fp.read()


image = get_file_content('1.png')
res_image = client.basicGeneral(image)
print(res_image)
res = res_image["words_result"]
print(res)
with open("result.txt", "w") as f:
    for content in res:
        print(content["words"])
        f.write("{}\n".format(content["words"]))

with open("result.txt", "r") as f:
    content = f.read()
# 语音合成
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
result = client.synthesis(content, 'zh', 1, {
    'vol': 5,  # 音量
    'spd': 5,  # 语速
    'pit': 6,  # 音调
    'per': 111,  # 音色
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)
# if __name__ == "__main__":
#    pass
