# python3
import base64
import json
import time
import urllib.parse
import urllib.request

with open('2.jpg', 'rb') as f:  # 以二进制读取本地图片
    data = f.read()
    encodestr = str(base64.b64encode(data), 'utf-8')
# 请求头
headers = {
    'Authorization': 'APPCODE 944163d47fa645c5b97a9bfea3c1d220',
    'Content-Type': 'application/json; charset=UTF-8'
}


def posturl(url, data=None):
    if data is None:
        data = {}
    try:
        params = json.dumps(data).encode(encoding='UTF8')
        req = urllib.request.Request(url, params, headers)
        r = urllib.request.urlopen(req)
        html = r.read()
        r.close();
        return html.decode("utf8")
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read().decode("utf8"))
    time.sleep(1)


if __name__ == "__main__":
    url_request = "https://ocrapi-advanced.taobao.com/ocrservice/advanced"
    dict = {'img': encodestr}

    html = posturl(url_request, data=dict)
    res = json.loads(html)
    with open('识别文字.txt', "x") as r:
        for word in res["prism_wordsInfo"]:
            print(word["word"])
            r.write("{}\n".format(word["word"]))
