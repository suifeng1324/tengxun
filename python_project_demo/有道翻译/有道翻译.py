import execjs
import requests

word = input("请输入要翻译的单词：")
# 用python代码调用js代码
with open("youdao.js", mode="r", encoding='UTF-8') as f:
    js_code = f.read()

js_data = execjs.compile(js_code)
# 调用js函数
sign = js_data.call('youdao', word)
# print(sign)

url = "https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
headers = {
    'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=182757865.2329147; _ga=GA1.2.1658155521.1646379865; OUTFOX_SEARCH_USER_ID="309051694@10.108.162.133"; P_INFO=null; fanyi-ad-id=305838; fanyi-ad-closed=0; ___rl__test__cookies=1653285708819',
    'Host': 'fanyi.youdao.com',
    'Origin': 'https://fanyi.youdao.com',
    'Referer': 'https://fanyi.youdao.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
}
# print(sign["salt"],sign["sign"],sign["ts"],sign["bv"])
data = {
    'i': word,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': sign["salt"],
    'sign': sign["sign"],
    'lts': sign["ts"],
    'bv': sign["bv"],
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',

}
respond = requests.post(url, data, headers)
# pprint.pprint(respond.json())


print("翻译的结果：", respond.json()["translateResult"][0][0]["tgt"])
