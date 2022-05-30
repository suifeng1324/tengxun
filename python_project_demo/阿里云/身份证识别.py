import base64
import json
import urllib.request

# API产品路径
host = 'https://personcard.market.alicloudapi.com'
path = '/ai_market/ai_ocr_universal/shen_fen_zheng/ch/v1'
# 阿里云APPCODE
appcode = '944163d47fa645c5b97a9bfea3c1d220'
url = host + path
bodys = {}
querys = ""

# 参数配置
# if False:
# 启用BASE64编码方式进行识别
# 内容数据类型是BASE64编码

f = open(r'sfz.jpg', 'rb')
contents = base64.b64encode(f.read())
f.close()
bodys['IMAGE'] = contents
bodys['IMAGE_TYPE'] = '0'
print("1")

# else:
#     #启用URL方式进行识别
#     #内容数据类型是图像文件URL链接
#     bodys['IMAGE'] = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589431574503&di=77e67a9f72c7f241347e7782307a48cb&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20191021%2F4afb486be6174a3fa473ea3216130933.jpeg'
#     bodys['IMAGE_TYPE'] = '1'
#     print("2")

post_data = urllib.parse.urlencode(bodys).encode('utf-8')

request = urllib.request.Request(url, post_data)
request.add_header('Authorization', 'APPCODE ' + appcode)
request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    res1 = content.decode('utf-8')
    print(res1, type(res1))
    res = json.loads(res1)
    name = res["身份证识别实体信息"]["身份证人像面实体信息"]["姓名"]
    sex = res["身份证识别实体信息"]["身份证人像面实体信息"]['性别']
    birthday = res["身份证识别实体信息"]["身份证人像面实体信息"]['出生日期']
    address = res["身份证识别实体信息"]["身份证人像面实体信息"]['住址']

    print("{},{},{},{}".format(name, sex, birthday, address))
    # name = res.
    # print()
    # print()
